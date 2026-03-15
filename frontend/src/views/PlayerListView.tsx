import { use, useEffect, useState } from 'react'
import { Button } from '../components/ui/button'
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow} from '../components/ui/table'
import { fetchPlayers } from '../api/PlayerService'
import type { Player } from '../types/Player';


export function PlayerListView() {
    const [players, setPlayers] = useState<Player[]>([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const players = await fetchPlayers();
                setPlayers(players);
            } catch (error) {
                console.error('Error fetching players:', error);
            } finally {
                setLoading(false);
            }
        };
        fetchData();
    }, [])

    return (
        <>
            <div className="flex items-center justify-between mb-4">
                <h3 className="text-2xl font-bold">Players</h3>
                <a href="/players/create">
                <Button variant="outline">
                    Add player
                </Button>
                </a>
            </div>
            <Table>
                <TableHeader>
                    <TableRow>
                        <TableHead>Name</TableHead>
                        <TableHead>Position</TableHead>
                        <TableHead>Team</TableHead>
                    </TableRow>
                </TableHeader>
                <TableBody>
                    {players.map((player) => (
                        <TableRow key={player.id}>
                            <TableCell>{player.firstname}</TableCell>
                            <TableCell>{player.lastname}</TableCell>
                            <TableCell>{player.country_code}</TableCell>
                        </TableRow>
                    ))}
                </TableBody>
            </Table>
        </>

    )
}