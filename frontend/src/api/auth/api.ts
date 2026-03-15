import axios from 'axios';

let headers: { [key: string]: string } = {};
const apiURL = import.meta.env.VITE_REACT_APP_API_URL || 'http://localhost:8000/';

const api = axios.create({
    baseURL: apiURL,
    headers: headers
});

export default api;