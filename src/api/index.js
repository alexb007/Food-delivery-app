import axios from 'axios';


export default axios.create({
    baseURL: 'http://15.188.194.70:8000/api',
    headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`
    }
});
