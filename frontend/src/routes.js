import Vue from 'vue';
import Router from 'vue-router';

//import components below
import Home from './components/Home.vue'; //input
import Dashboard from './components/Dashboard.vue';
import Review from './components/Review.vue';
import Feed from './components/Feed.vue'; //live feed 


Vue.use(Router);

let router = new Router({
    routes: [
        { path: '/', component: Home },
        //Add routes
        { path: '/dashboard', component: Dashboard, name: 'dashboard'},
        { path: '/review', component: Review, name: 'review'},
        { path: '/feed', component: Feed, name: 'feed'},
   
    ],
    mode: 'history'
});

export default router;