<template id = "a">
  <div>
    <v-app-bar color="#5b2c86" height = "100px">
       <div id="logo">
          <router-link class="rlink" to="/"><v-img height="70px" width = "50px" src="https://drive.google.com/uc?export=download&id=1Q_XJ7rkGiF2C6HLj4zJmti8EnKdcWNk6"></v-img></router-link>
      </div>
      <v-spacer></v-spacer>
    
      <v-btn class="b1" to="/" text>Input</v-btn>
       <v-spacer></v-spacer>
      <v-btn class="b1" to="/review" text>Review</v-btn>
    <v-spacer></v-spacer>
      <v-btn class="b1" to="/feed" text>Live Feed</v-btn>
    <v-spacer></v-spacer>
      <v-btn class="b1" to="/dashboard" text>Dashboard</v-btn>
    <v-spacer></v-spacer>
   
    </v-app-bar>
  </div>
</template>

<script>
export default {
  data: () => ({

  })
};
</script>

<style scoped>

.rlink {
  color: #FFF;
  text-decoration: none;
  font-weight: 550;
  font-size: 0.4cm;
  margin: 0.5cm;
}

.b1{
    color: white!important;
    font-family: "Roboto";
    font-weight: 550;
}
</style>