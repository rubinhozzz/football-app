import { Button } from '../components/ui/button'
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow} from '../components/ui/table'


export function LocationListView() {

    const locations = [
        {
            name: 'Stadium A',
            address: '123 Main St, City A',
            capacity: 50000
        },
        {
            name: 'Stadium B',
            address: '456 Elm St, City B',
            capacity: 40000
        }
    ]
    return (
        <>
            <div className="flex items-center justify-between mb-4">
                <h3 className="text-2xl font-bold">Locations</h3>
                <a href="/locations/create">
                <Button variant="outline">
                    Add location
                </Button>
                </a>
            </div>
            <Table>
                <TableHeader>
                    <TableRow>
                        <TableHead>Name</TableHead>
                        <TableHead>Address</TableHead>
                        <TableHead>Capacity</TableHead>
                    </TableRow>
                </TableHeader>
                <TableBody>
                    {locations.map((location) => (
                        <TableRow key={location.name}>
                            <TableCell>{location.name}</TableCell>
                            <TableCell>{location.address}</TableCell>
                            <TableCell>{location.capacity}</TableCell>
                        </TableRow>
                    ))}
                </TableBody>
            </Table>
        </>

    )
}