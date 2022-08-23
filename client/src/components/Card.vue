<template>
    <div class="card mb-5 rounded-5 shadow">
        <div class="py-3 card-header">
            <h4 class="my-0 fw-normal">{{ product.title }}</h4>
        </div>
        <div class="card-body my-card">
            <img v-if="product.image" class="product-image" :src=product.image alt="picture"/>
            <img v-else class="product-image" src="../../public/assets/none.jpg" alt="picture"/>
            <div class="inner-card">
                <h1 class="card-title pricing-card-title">{{ product.price }}<small class="text-muted fw-light">₽</small></h1>
                <ul class="list-unstyled mt-3 mb-1">
                    <li v-if="product.description">{{ product.description }}</li>
                    <br/>
                    <li>Осталось {{ product.quantity}} шт.</li>
                </ul>
            </div>
        </div>
        <button @click="buyItem(product)" type="submit" class="btn btn-lg btn-outline-primary my-btn add_item">Купить</button>
    </div>
</template>

<script>
export default {
    name: 'Card',
    props: {
        product: {
            type: Object,
            require: true
        },
    },
    methods: {
        buyItem(product){
            this.$store.commit('addItem', product)
            this.$emit('update_basket_count');
        },
    }
}
</script>

<style scoped>
.card_header {
    background-color: rgb(224, 247, 248) !important;
    border-top-left-radius: 30px !important;
    border-top-right-radius: 30px !important;
}

.my-card {
    display: flex;
    flex-direction: row;
    justify-content: space-around;
}

.product-image {
    object-fit: cover;
    object-position: 50% 50%;
    width: 40%;
    height: 40%;
    border-radius: 20px;
    align-self: center;
}

.inner-card {
    display: flex;
    flex-direction: column;
    padding: 10% 10% 10% 10%;
}

.add_item {
    margin: 0 auto;
    margin-bottom: 10px;
    max-width: 150px;

}
</style>