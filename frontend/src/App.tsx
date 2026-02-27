import './App.css'
import { Route, Routes, BrowserRouter } from 'react-router-dom'
import { Layout }  from './components/Layout'
import { PlayerListView } from './views/PlayerListView'
import { MatchListView } from './views/MatchListView'
import { PlayerCreateView } from './views/PlayerCreateView'
import { LocationListView } from './views/LocationListView'

function App() {
    return (
        <>
        <BrowserRouter>
            <Routes>
                <Route element={<Layout />}>
                    <Route path='/' element={<div>Dashboard</div>} />
                    <Route path="/matches" element={<MatchListView />} />
                    <Route path="/players" element={<PlayerListView />} />
                    <Route path="/players/create" element={<PlayerCreateView />} />
                    <Route path="/locations" element={<LocationListView />} />
                </Route>
            </Routes>
        </BrowserRouter>
        </>
    )
}

export default App
