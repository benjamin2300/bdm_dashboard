<template>
  <div class="home">
    
    <ShowDataComponent  />
  </div>
</template>

<script>
// @ is an alias to /src
// import { apiService } from "@/common/api.service.js";
import ShowDataComponent from "@/components/ShowData.vue";

export default {
  name: "home",
  components: {
    ShowDataComponent
  },
  data() {
    return {
      employees: [],
    }
  },
  methods: {
    // getEmployees()
  }
};
</script>
