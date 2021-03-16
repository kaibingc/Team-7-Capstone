import Vue from 'vue';
import App from './App.vue';
import vuetify from './plugins/vuetify' // path to vuetify export

// These are the routes we're going to create.
import router from './routes'

// The usual app stuff goes here.

new Vue({
  //
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app');
