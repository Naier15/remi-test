<template>
    <Header :basket_count="basket_count" />
    <div class="row row-cols-1 row-cols-md-3 mb-3 text-center offset">
        <div v-if="basket" class="col my_col" v-for="(product, index) in basket" :key="product.id">
            <BasketCard 
                v-on:increase="increase"
                v-on:decrease="decrease"
                :product="product"
                :index="index" />
        </div>
        <div v-else class="my_col"><b>Ваша корзина пустует</b></div>
    </div>
    <Footer />
</template>

<script>
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'
import BasketCard from '@/components/BasketCard.vue'

export default {
    name: 'Basket',
    components: {
        Header, Footer, BasketCard
    }, 
    data() {
        return {
            basket_count: null,
            basket: null,
        }
    },
    methods: {
        get_basket_count() {
            this.basket_count = this.$store.getters.basket_count
        },
        get_basket(ret=false) {
            let storage = localStorage.getItem('my_basket') 
            this.basket = storage === null ? null : Object.values(JSON.parse(storage))
            if (ret){
                return this.basket
            }
        },
        increase(id) {
            let basket = this.get_basket(true)
            basket[id]['quantity'] += 1
            localStorage.setItem('my_basket', JSON.stringify(basket, null, 4)) 
            this.get_basket_count()
        }, 
        decrease(id) {
            let basket = this.get_basket(true)
            if (basket[id]['quantity'] > 0){
                basket[id]['quantity'] -= 1
            }
            localStorage.setItem('my_basket', JSON.stringify(basket, null, 4)) 
            this.get_basket_count()
        },
    },
    mounted() {
        this.get_basket_count()
        this.get_basket()
    }
}
</script>

<style scoped>
.offset {
    margin-top: 110px !important;
    max-width: 800px;
    margin-left: auto !important;
    margin-right: auto !important;
}

.my_col {
    width: 80% !important;
    margin: 0 auto;
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