<template lang="html">
    <div class="container">
        <div class="row">
            <div class="col text-left">
            <div class="">
                <h2>Listado de Libros</h2>
                <b-button size="sm"  variant="primary" :to="{ name:'NewBook' }">
                    Nuevo Libro
                </b-button>
            </div>
            <br>
            <div class="col-md-12">
                <b-table striped hover :items="books" :fields="fields">
                    <template  v-slot:cell(action)="data">
                        <b-button size="sm" variant="primary" :to="{ name:'EditBook', params: {bookId: data.item.id} }">
                            Editar
                        </b-button>
                        <b-button size="sm" variant="danger">
                            Eliminar
                        </b-button>
                    </template>
                </b-table>
            </div>
            </div>
        </div>
    </div> 
</template>

<script>
import axios from 'axios';

export default {
    data () {
        return {
            fields : [
                { key: 'title', label: 'Título' },
                { key: 'description', label: 'Descripción' },
                { key: 'action', label: 'Acción' }
            ],
            books: []
        }
    },
    methods: {
        getBooks () {
            const path =  `${process.env.BASE_URL}api/books/`
            axios.get(path).then((response) => {
                this.books = response.data
            }).catch((error) => {
                console.log(error)
            })
        }
    },
    created() {
        this.getBooks()
    }, 
}
</script>
<style lang="css" scoped>
</style>