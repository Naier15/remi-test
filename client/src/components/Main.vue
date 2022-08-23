<template>
    <div class="content_block offset">
        <div v-if="!$store.state.loading" class="spinner-grow my_spinner" style="width: 3rem; height: 3rem; " role="status">
            <span class="visually-hidden">Загрузка...</span>
        </div>
        <div v-else-if="$store.state.products.length > 0">
            <div class="row row-cols-1 row-cols-md-3 mb-3 text-center">
                <div class="col" v-for="(product, index) in $store.state.products" :key="product.id">
                    <Card 
                        @update_basket_count="update_basket_count"
                        :product="product" />
                </div>
            </div>
        </div>
        <h2 v-else class="my_spinner">Список пока пуст</h2> 
    </div>
</template>

<script>
import Card from '@/components/Card.vue'

export default {
    name: 'Main',
    components: {
        Card,
    },
    data() {
        return {
            createVisible: false,
            editVisible: false,
            selectedOrder: null
        }
    },
    methods: {
        showDetails() {
          this.createVisible = true
        },
        showEdit(order){
          this.selectedOrder = order
          this.editVisible = true
        },
        update_basket_count() {
            this.$emit('update_basket_count');
        }
    },
    created() {
      this.$store.dispatch('getProducts')
    }
}
</script>

<style scoped>
.offset {
    margin-top: 110px !important;
    margin-left: auto !important;
    margin-right: auto !important;
}

.list_pages {
	text-align: center;
	margin: 0 0 20px 0;
}
.list_pages ul {
	margin: 20px 0 0 0;
	padding: 0;
	list-style: none;
}
.list_pages ul li {
	display: inline-block;
	margin: 0 20px 0 0;
}
.list_pages a {
	color: #000;
	font-size: 24px;
	text-decoration: none;
}
.list_pages .page_num, .page_num_selected {
	display: inline-block;
	width: 60px;
	height: 44px;
	border: 1px solid #d0d0d0;
	border-radius: 30px;
}
.list_pages .page_num:hover {
	box-shadow: 3px 3px 1px #d0d0d0; 
}
.list_pages .page_num_selected {
	border: none;
	color: #000;
	font-size: 20px;
}
.list_pages .page_num_selected:hover {
	box-shadow: none; 
}

.content_block {
    display: flex;
    justify-content: center;
    flex-direction: column;
}
.my_spinner {
    margin: 0 auto;
    margin-bottom: 30px;
}
</style>