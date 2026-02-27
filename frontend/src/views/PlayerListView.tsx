import { Button } from '../components/ui/button'
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow} from '../components/ui/table'


export function PlayerListView() {
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
                    <TableRow>
                        <TableCell>Lionel Messi</TableCell>
                        <TableCell>Forward</TableCell>
                        <TableCell>Paris Saint-Germain</TableCell>
                    </TableRow>
                    <TableRow>
                        <TableCell>Cristiano Ronaldo</TableCell>
                        <TableCell>Forward</TableCell>
                        <TableCell>Manchester United</TableCell>
                    </TableRow>
                </TableBody>
            </Table>
        </>

    )
}