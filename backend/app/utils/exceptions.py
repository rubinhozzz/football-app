class NotFoundException(Exception):
    pass

class PlayerCannotBeDeletedException(Exception):
    def __init__(self, player_id: int):
        super().__init__(f"Player with id {player_id} cannot be deleted because they are associated with existing matches.")

class PlayerNotFoundException(NotFoundException):
    def __init__(self, player_id: int):
        super().__init__(f"Player with id {player_id} not found.")


class MatchNotFoundException(NotFoundException):
    def __init__(self, match_id: int):
        super().__init__(f"Match with id {match_id} not found.")

class MatchCannotBeDeletedException(Exception):
    def __init__(self, match_id: int):
        super().__init__(f"Match with id {match_id} cannot be deleted because it is associated with existing players.")