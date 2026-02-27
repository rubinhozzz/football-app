from typing import Optional
from datetime import datetime, timezone
from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy import Boolean, ForeignKey, String, LargeBinary, DateTime
from app.database.database import Base
from enum import Enum
from sqlalchemy import Enum as SQLEnum


class Team(Enum):
    A = 'A'
    B = 'B'


class AuditMixin:
    created_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=True)
    created_by: Mapped[Optional[int]] = mapped_column(ForeignKey("users.id"), nullable=True)
    last_update_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=True)
    updated_by: Mapped[Optional[int]] = mapped_column(ForeignKey("users.id"), nullable=True)


class PlayerMatch(Base):
    __tablename__ = 'players_matches'
    player_id: Mapped[int] = mapped_column(ForeignKey("players.id"), primary_key=True)
    match_id: Mapped[int] = mapped_column(ForeignKey("matches.id"), primary_key=True)
    team: Mapped[Team] = mapped_column(SQLEnum(Team), nullable=False)
    player: Mapped["Player"] = relationship(back_populates="match_assocations", lazy="noload")
    match: Mapped["Match"] = relationship(back_populates="player_associations", lazy="noload")
    pichichi: Mapped[bool] = mapped_column(Boolean, server_default='f', default=False)


class User(Base, AuditMixin):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(100))
    hashed_password: Mapped[str] = mapped_column(String(100))
    is_active: Mapped[bool] = mapped_column(Boolean, server_default='t', default=True)


class Player(Base, AuditMixin):
    __tablename__ = "players"
    id: Mapped[int] = mapped_column(primary_key=True)
    firstname: Mapped[str] = mapped_column(String(50), nullable=False)
    lastname: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    country_code: Mapped[Optional[str]] = mapped_column(String(3), nullable=True)
    photo: Mapped[Optional[bytes]] = mapped_column(LargeBinary(), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, server_default='t', default=True)
    match_mvp: Mapped["Match"] = relationship(back_populates="mvp", lazy="noload")
    matches: Mapped[list["Match"]] = relationship(back_populates="players", lazy="noload", secondary="players_matches", viewonly=True)
    match_assocations: Mapped[list["PlayerMatch"]] = relationship(back_populates="player", lazy="noload")


class Match(Base, AuditMixin):
    __tablename__ = "matches"
    id: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.now)
    duration_minutes: Mapped[Optional[int]] = mapped_column(nullable=True, default=0, server_default="0")
    teamA_name: Mapped[str] = mapped_column(String(100), nullable=False)
    teamB_name: Mapped[str] = mapped_column(String(100), nullable=False)
    teamA_score: Mapped[Optional[int]] = mapped_column(default=0, nullable=True)
    teamB_score: Mapped[Optional[int]] = mapped_column(default=0, nullable=True)
    location_id: Mapped[Optional[int]] = mapped_column(ForeignKey("locations.id"), nullable=True)
    location: Mapped[Optional["Location"]] = relationship(back_populates="matches", lazy='noload')
    mvp_id: Mapped[Optional[int]] = mapped_column(ForeignKey("players.id"), nullable=True)
    mvp: Mapped[Optional["Player"]] = relationship(back_populates="match_mvp", lazy="noload")
    players: Mapped[list["Player"]] = relationship(back_populates="matches", lazy="noload", secondary="players_matches", viewonly=True)
    player_associations: Mapped[list["PlayerMatch"]] = relationship(back_populates="match", lazy="noload")


class Location(Base, AuditMixin):
    __tablename__ = "locations"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, unique=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    postcode: Mapped[Optional[str]] = mapped_column(String(10), nullable=True)
    address: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, server_default='t', default=True)
    matches: Mapped[list["Match"]] = relationship(back_populates="location", lazy="noload")
