import { Input } from "../ui/input";
import { Field, FieldLabel } from "../ui/field";
import { Button } from "../ui/button";


export function PlayerForm() {
    return (
        <>
            <Field>
                <FieldLabel>Name</FieldLabel>
                <Input
                    type="text"
                    placeholder="Name"
                    className="mb-4"
                />
            </Field>
            <Field>
                <FieldLabel>Position</FieldLabel>
                <Input
                    type="text"
                    placeholder="Position"
                    className="mb-4"
                />
            </Field>
            <Field>
                <FieldLabel>Team</FieldLabel>
                <Input
                type="text"
                placeholder="Team"
                className="mb-4"
            />
            </Field>
            <Button variant="outline" type="submit">
                Save
            </Button>
        </>
    )
}