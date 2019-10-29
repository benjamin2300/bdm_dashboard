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
import { apiService } from "@/common/api.service.js"

export default {
  name: "home",
  data() {
    return {
      employees: [],
    }
  },
  methods: {
    getEmployees() {
      let endpoint = "api/employees/";
      apiService(endpoint)
        .then(data => {
          this.employees.push(...data.results);

        })
    }
  },
  created() {
    this.getEmployees()
  }
};
</script>

<style scoped>
.employee-name {
  font-weight: bold;
  color: red;
}
.employee-position {
  font-weight: bold;
  color: blue;
}
</style>