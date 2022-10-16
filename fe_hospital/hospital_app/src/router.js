import { createRouter, createWebHashHistory } from 'vue-router';
import App from './App.vue';
import LogIn from './components/LogIn.vue'
import SignUp from './components/SingUp.vue'
import Home from './components/Home.vue'
import RequestUser from './components/RequestUser.vue'
import DeleteUser from './components/DeleteUser.vue'
import PutUser from './components/PutUser.vue'
import Postpsalud from './components/Postpsalud.vue'
import deletepsalud from './components/deletepsalud.vue'
import getpsalud from './components/getpsalud.vue'
import putpsalud from './components/putpsalud.vue'

const routes = [
  {
    path: '/',
    name: 'root',
    component: App
  },  
  {
    path: '/user/logIn',
    name: 'logIn',
    component: LogIn
  },
  {
    path: '/user/signUp',
    name: 'signUp',
    component: SignUp
  },
  {
    path: '/user/Home',
    name: 'Home',
    component: Home
  },    
  {
    path: '/user/RequestUser',
    name: 'RequestUser',
    component: RequestUser
  },
  {
    path: '/user/DeleteUser',
    name: 'DeleteUser',
    component: DeleteUser
  },
  {
    path: '/user/PutUser',
    name: 'PutUser',
    component: PutUser
  },
  {
    path: '/user/Postpsalud',
    name: 'Postpsalud',
    component: Postpsalud
  },
  {
    path: '/user/deletepsalud',
    name: 'deletepsalud',
    component: deletepsalud
  },
  {
    path: '/user/getpsalud',
    name: 'getpsalud',
    component: getpsalud
  },
  {
    path: '/user/putpsalud',
    name: 'putpsalud',
    component: putpsalud
  }            
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
})

export default router;


