import axios from 'axios';
const API_URL = 'http://localhost:8000';

export class APIService {
  constructor() {

  }
  getEmployees() {
    const url = `${API_URL}/api/employees/`;
    return axios.get(url).then(response => response.data);
  }
  getEmployee(pk) {
    const url = `${API_URL}/api/employees/${pk}`;
    return axios.get(url).then(response => response.data);
  }
}