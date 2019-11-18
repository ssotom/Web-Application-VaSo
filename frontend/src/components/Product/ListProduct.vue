<template lang="html">
  <div>
    <div class="row">
        <div class="col d-flex flex-grow-1 align-items-baseline">
            <h2>Nuestros Productos</h2>
            <b-button variant="outline-primary" class="ml-auto " @click="giveOpinion">Danos tu opinión!</b-button>
        </div>
    </div>
    <div>

    <b-toast id="my-toast" solid no-auto-hide  toaster="b-toaster-bottom-right">
      <template v-slot:toast-title>
        <div class="d-flex flex-grow-1 align-items-baseline">
          <strong class="mr-auto">Danos tu opinión!</strong>
        </div>
      </template>
      <p>Selecciona los productos sobre los cuales quieres dejar tu opinión. </p>
      <b-form @submit.prevent="sendOpinion">
        <b-form-textarea
        id="textarea"
        v-model="text"
        placeholder="¿Qué piensas de nuestros productos?"
        rows="4"
        max-rows="5"
        no-resize>
        </b-form-textarea>
        <b-button type="submit" class="mt-2" block variant="primary">Enviar</b-button>
       </b-form>
    </b-toast>
    </div>
    <br>
    <div class="row">
    <template v-for="product in products">
    <div class="col-lg-3 mt-4">
        <div class="card">
        <div class="card-body">
            <div class="d-flex flex-grow-1 align-items-baseline">
                <h5 class="card-title">{{product.name}}</h5>
                <b-form-checkbox v-show="opinion" class="ml-auto" v-model="selected" name="checkbox-{product.id}" v-bind:value="product.id">
                </b-form-checkbox>
            </div>
            <img v-bind:src="product.picture" class="rounded mx-auto d-block">
            <p class="card-text">{{product.description}}</p>
        </div>
        </div>
    </div>
    </template>
    </div> 
  </div>
</template>

<script>
import axios from 'axios';

export default {
    data () {
        return {
            products: [],
            selected: [],
            text: '',
            opinion: false
        }
    },
    methods: {
        getProducts () {
            const path =  `${process.env.BASE_URL}api/products/`
            axios.get(path).then((response) => {
                this.products = response.data
            }).catch((error) => {
                console.log(error)
            })
        },
        giveOpinion() {
            this.$bvToast.show('my-toast')
            this.opinion = true
        },
        sendOpinion() {
            
        },
        createProducts() {
            const path = `${process.env.BASE_URL}api/products/`
            for (var _i = 1; _i <= 50; _i++) {
                let products2 = {
                    name : "Producto "+_i,
                    description : "Descripción del producto "+_i,
                    picture: "https://img.icons8.com/plasticine/200/000000/used-product.png"
                }
                setTimeout(() => {    
                    axios.post(path, products2).then((response) => {

                    }).catch((error) => {
                        console.log(error)
                    })
                }, 1000)
            }
        },
    },
    created() {
        this.getProducts()
        //this.createProducts()
    }, 
}
</script>
<style lang="css" scoped>
</style>