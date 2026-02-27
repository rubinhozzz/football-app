import { Outlet } from "react-router-dom"
import { SidebarProvider, Sidebar, SidebarHeader, SidebarContent, SidebarMenu, SidebarMenuItem, SidebarGroup, SidebarTrigger } from "./ui/sidebar"

export function Layout() {
    return (
        <SidebarProvider>
            <Sidebar variant="inset">
                <SidebarHeader>
                    <h1 className="text-2xl font-bold">Football Manager</h1>
                </SidebarHeader>
                <SidebarContent>
                    <SidebarGroup title="Main">
                        <SidebarMenu>
                            <SidebarMenuItem key="dashboard"><a href="/">Dashboard</a></SidebarMenuItem>
                            <SidebarMenuItem key="matches"><a href="/matches">Matches</a></SidebarMenuItem>
                        </SidebarMenu>
                    </SidebarGroup>
                    <SidebarGroup title="Maintenance">
                        <SidebarMenu>
                            <SidebarMenuItem key="players"><a href="/players">Players</a></SidebarMenuItem>
                            <SidebarMenuItem key="locations"><a href="/locations">Locations</a></SidebarMenuItem>
                        </SidebarMenu>
                    </SidebarGroup>
                </SidebarContent>
            </Sidebar>
            <main className="flex-1 p-6">
                <SidebarTrigger />
                <Outlet />
            </main>
        </SidebarProvider>
    )
}