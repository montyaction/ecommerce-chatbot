import axios from 'axios';

const baseURL = 'https://2dbfc692-c657-40ba-853a-41081bce151b.mock.pstmn.io';
// const baseURL1 = process.env.REACT_APP_API_BASE_URL;
// const baseURL2 = import.meta.env.REACT_APP_API_BASE_URL;

// console.log(baseURL1);
// console.log(baseURL2);

const api = axios.create({
  baseURL: baseURL || 'http://localhost:3001', // Use environment variable or default
  withCredentials: true // If you need to send cookies with requests
});

export default api;