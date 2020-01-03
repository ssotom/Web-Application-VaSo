import Vue from 'vue'
import Router from 'vue-router'
import store from '@/store.js'
import ListBook from '@/components/Book/ListBook'
import EditBook from '@/components/Book/EditBook'
import NewBook from '@/components/Book/NewBook'
import Login from '@/components/Authentication/Login'
import Register from '@/components/Authentication/Register'
import ListProduct from '@/components/Product/ListProduct'

Vue.use(Router)

let router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Productos',
      component: ListProduct
    },
    {
      path: '/login',
      name: 'Login',
      component:Login,
      meta: { 
        guest: true
      }
    },
    {
      path: '/register',
      name: 'Register',
      component:Register,
      meta: { 
        guest: true
      }
    },
  ]
})

router.beforeEach((to, from, next) => {
  if(to.matched.some(record => record.meta.requiresAuth)) {
    if (store.getters.isLoggedIn) {
      next()
      return
    }
    next('/login') 
  } else if(to.matched.some(record => record.meta.guest)) {
    if (store.getters.isLoggedIn) {
      next('/')
      return
    }
    next() 
  } else {
    next() 
  }
})

export default router
