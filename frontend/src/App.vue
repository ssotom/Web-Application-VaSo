<template>
<div id="app">
<div id="nav" class="mb-4">
  <b-navbar size="sm" toggleable="lg" type="dark" variant="primary">
    <b-navbar-brand to="/">VaSo</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        
      </b-navbar-nav>

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto" >
        <b-nav-item to="/login" v-show="!isLoggedIn">Login</b-nav-item>
        <b-nav-item to="/register" v-show="!isLoggedIn">Register</b-nav-item>
        <b-nav-item-dropdown right v-show="isLoggedIn">
          <!-- Using 'button-content' slot -->
          <template v-slot:button-content>
            <em>Usuario</em>
          </template>
          <b-dropdown-item href="">Profile</b-dropdown-item>
          <b-dropdown-item @click="logout">Sign Out</b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</div><div class="container-fluid">
  <router-view/>
</div>

</div>

</template>

<script>
export default {
  name: 'App',
  computed : {
      isLoggedIn : function(){ return this.$store.getters.isLoggedIn}
  },
  methods: {
    logout: function () {
      this.$store.dispatch('logout')
      .then(() => {
        this.$router.push('/login')
      })
    }
  },
  created: function () {
    this.$http.interceptors.response.use(undefined, function (err) {
      return new Promise(function (resolve, reject) {
        if (err.status === 401 && err.config && !err.config.__isRetryRequest) {
          this.$store.dispatch(logout)
        }
        throw err;
      });
    });
  }
}
</script>

<style>
.form-group input {
  height: 50px; 
}
.btn-lg {
  height: 60px; 
}
</style>
