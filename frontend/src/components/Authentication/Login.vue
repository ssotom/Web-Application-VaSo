<template>
  <div class="container">
    <div class="mb-3">
      <h2>Inciar Sesión</h2>
    </div>
    <b-form @submit.prevent="login">
      <b-form-group id="input-group-1" label="Usuario" label-for="username">
        <b-form-input
          id="username"
          v-model="username"
          type="text"
          required
          placeholder="Usuario">
        </b-form-input>
      </b-form-group>
      <b-form-group id="input-group-2" label="Contraseña" label-for="password">
        <b-form-input
          id="password"
          type="password"
          v-model="password"
          required
          placeholder="Contraseña">
        </b-form-input>
      </b-form-group>
      <b-button type="submit" block size="lg" variant="primary">Inciar Sesión</b-button>
    </b-form>
    <center><b-spinner class="mt-2" variant="primary" type="grow" label="Spinning" v-if="spinner"></b-spinner></center>
  </div>
</template>

<script>
  export default {
    data(){
      return {
        username : "",
        password : "",
        spinner : false,
      }
    },
    methods: {
      login: function () {
        this.spinner = true
        let username = this.username 
        let password = this.password
        this.$store.dispatch('login', { username, password }) 
       .then((resp) => {
        this.$router.push('/')
       }).catch(err => { 
         this.spinner = false
         console.log(err.response.data) 
       })
      }
    },
  }
</script>