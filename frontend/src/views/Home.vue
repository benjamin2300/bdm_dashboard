<template>
  <div class="home">
    <div class="container">

      <div v-for="employee in employees" :key="employee.pk">
        <span class="employee-name">Name : {{ employee.name }}</span>
        <span class="employee-position">Position : {{ employee.position }}</span> 
        <hr>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import { APIService } from "@/common/APIService.js";
const API_URL = "http://localhost:8000";
const apiService = new APIService()

export default {
  name: "home",
  data() {
    return {
      employees: [],
    }
  },
  methods: {
    getEmployees() {
      apiService.getEmployees()
        .then(data => {
          this.employees = data
        })
    }
  },
  created() {
    this.getEmployees()
  },
};
</script>

<style scoped>
.employee-name {
  font-weight: bold;
  color: red;
  display: block;
}
.employee-position {
  font-weight: bold;
  color: blue;
  display: block;
}

</style>