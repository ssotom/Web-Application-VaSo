<template>
<div class="container">
  <div class="mb-3">
     <h2>Registrarse</h2>
  </div>
  <form @submit.prevent="registerLogin">
    <div class="row">
      <div class="col-md-6">
        <b-form-group id="input-group-1" label="Nombre completo" label-for="name">
        <b-form-input
          id="name"
          v-model="customer.name"
          type="text"
          required
          placeholder="Nombre completo">
        </b-form-input>
        </b-form-group>
      </div>
      <div class="col-md-6">
        <b-form-group id="input-group-1" label="Dirección" label-for="adress">
        <b-form-input
          id="adress"
          v-model="customer.adress"
          type="text"
          required
          placeholder="Dirección">
        </b-form-input>
        </b-form-group>
      </div>
    </div>

    <div class="row">
      <div class="col-md-4">
        <b-form-group id="input-group-1" label="Ciudad" label-for="city">
        <b-form-input
          id="city"
          v-model="customer.city"
          type="text"
          required
          placeholder="Ciudad">
        </b-form-input>
        </b-form-group>
      </div>
      <div class="col-md-4">
        <b-form-group id="input-group-1" label="Fecha nacimiento" label-for="birth">
        <b-form-input
          id="birth"
          v-model="customer.birth"
          type="date"
          required
          placeholder="Fecha nacimiento">
        </b-form-input>
        </b-form-group>
      </div>
      <div class="col-md-4">
        <b-form-group id="input-group-1" label="Correo electronico" label-for="email">
        <b-form-input
          id="email"
          v-model="customer.email"
          type="text"
          required
          placeholder="Correo electronico">
        </b-form-input>
        </b-form-group>
      </div>
    </div>

    <div class="row">
      <div class="col-md-4">
        <b-form-group id="input-group-1" label="Usuario" label-for="username">
        <b-form-input
          id="username"
          v-model="login.username"
          type="text"
          required
          placeholder="Usuario">
        </b-form-input>
        </b-form-group>
      </div>
      <div class="col-md-4">
        <b-form-group id="input-group-1" label="Contraseña" label-for="password">
        <b-form-input
          id="password"
          v-model="login.password"
          type="password"
          required
          placeholder="Contraseña"
          minlength="8">>
        </b-form-input>
        </b-form-group>
      </div>
      <div class="col-md-4">
        <b-form-group id="input-group-1" label="Confirmar contraseña" label-for="re_password">
        <b-form-input
          id="re_password"
          v-model="login.re_password"
          type="password"
          required
          placeholder="Confirmar contraseña"
          minlength="8">
        </b-form-input>
        </b-form-group>
      </div>
    </div>
    <b-button type="submit" block size="lg" variant="primary">Registrarse</b-button>
  </form>
  <center><b-spinner class="mt-2" variant="primary" type="grow" label="Spinning" v-if="spinner"></b-spinner></center>
  <b-alert
      v-model="showBottom"
      class="position-fixed fixed-bottom m-0 rounded-0"
      style="z-index: 2000;"
      variant="danger"
      dismissible
    >
      {{text}}
    </b-alert>
</div>
</template>

<script>
import axios from 'axios';
import swal from 'sweetalert'

  export default {
    data(){
      return {
        login: {
          username: '',
          password: '',
          re_password:'',
        },
        customer: {
          id: '',
          name: '',
          adress: '',
          city: '',
          birth: '',
          email: '',
        },
        spinner : false,
        text: '',
        showBottom: false,
      }
    },
    methods: {
      registerLogin() {
        if (this.login.password === this.login.re_password) {
            this.spinner = true
            this.$store.dispatch('register', this.login)
            .then((resp) => this.registerCustomer(resp))
            .catch(err => {
              this.spinner = false
              this.text = err.response.data
              this.showBottom = true
              console.log(err)
            })
          }else{
              this.text = "La contraseñas no coinciden"
              this.showBottom = true
          }
      },
      registerCustomer(resp) {
          this.customer.id = resp.data.id        
          const path = `${process.env.BASE_URL}api/customers/`
          axios.post(path, this.customer).then((response) => {
              this.$router.push('/login')
              swal("Registrado con exito!", "", "success")
          }).catch((error) => {
              this.spinner = false
              console.log(error.response.data)
          })
        },
    }
  }
</script>