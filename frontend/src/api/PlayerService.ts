import type { Player } from '../types/Player';
import api from './auth/api';

export const fetchPlayers = async (): Promise<Player[]> => {
    try {
        const url = `/players`;
        const { data } = await api.get(url);
        return data;
    } catch (error) {
        console.error('Failed to fetch players:', error);
        throw error;
    }
};