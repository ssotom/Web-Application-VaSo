import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    status: '',
    token: localStorage.getItem('token') || '',
    user : localStorage.getItem('user') || {},
  },
  mutations: {
    auth_request(state){
      state.status = 'loading'
    },
    auth_success(state, token, user){
      state.status = 'success'
      state.token = token
      state.user = user
    },
    auth_error(state){
      state.status = 'error'
    },
    logout(state){
      state.status = ''
      state.token = ''
      state.user = {}
    },
  },
  actions: {
    login({commit}, user){
      return new Promise((resolve, reject) => {
        commit('auth_request')
        axios({url: 'http://localhost:8000/auth/token/login/', data: user, method: 'POST' })
        .then(resp => {
          const token = resp.data.auth_token
          axios.defaults.headers.common['Authorization'] = 'Token ' + token
          axios({url: 'http://localhost:8000/auth/users/me/', method: 'GET' })
          .then(resp => {
            const user = JSON.stringify(resp.data)
            localStorage.setItem('token', token)
            localStorage.setItem('user', user)
            commit('auth_success', token, user)
          resolve(resp)
          }).catch(err => {
            commit('auth_error')
            localStorage.removeItem('token')
            localStorage.removeItem('user')
            reject(err)
          })
        })
        .catch(err => {
          commit('auth_error')
          reject(err)
        })
      })
    },
    register({commit}, user){
      return new Promise((resolve, reject) => {
        commit('auth_request')
        const path = `${process.env.BASE_URL}auth/users/`
        axios.post(path, user).then((resp) => {
          resolve(resp)
        }).catch((err) => {
          commit('auth_error', err)
          localStorage.removeItem('token')
          reject(err)
        })
      })
    },
    logout({commit}){
      return new Promise((resolve, reject) => {
        axios({url: 'http://localhost:8000/auth/token/logout/', method: 'POST' })
        commit('logout')
        localStorage.removeItem('token')
        localStorage.removeItem('user')
        delete axios.defaults.headers.common['Authorization']
        resolve()
      })
    },
  },
  getters : {
    isLoggedIn: state => !!state.token,
    authStatus: state => state.status,
  }
})