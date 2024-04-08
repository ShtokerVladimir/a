<script setup lang="ts">
import InputText from 'primevue/inputtext'
import { onMounted, ref } from 'vue'
import ButtonComponent from '../components/ButtonComponent.vue'
import Header from '../components/Header.vue'
import { useTestStore } from '../stores/test.store'

const testStore = useTestStore()
const tests = ref()

onMounted(() => {
	tests.value = testStore.tests
})
</script>

<template>
	<Header />
	<main>
		<section class="search_test">
			<h1>Поиск</h1>
			<div class="search_block">
				<div class="search_field">
					<InputText type="text" :style="{ width: '100%' }" />
					<ButtonComponent label="Поиск" @click="() => {}" />
				</div>
				<ButtonComponent label="Создать новый тест" @click="() => {}" />
			</div>
		</section>
		<section class="test_list">
			<h1>Тесты</h1>
			<div class="test_table">
				<div class="header_table">
					<div>Название</div>
					<div>Дата и время</div>
					<div>Макс. балл</div>
				</div>
				<div class="body_table" v-for="(test, index) in tests" :key="index">
					<div>{{ test.name }}</div>
					<div>{{ test.date }}</div>
					<div>{{ test.max_score }}</div>
				</div>
			</div>
		</section>
	</main>
</template>

<style scoped>
main {
	display: flex;
	flex-direction: column;
	height: calc(100vh - 60px);
	padding: 0 360px;
	> section {
		margin-block: 20px;
		display: flex;
		flex-direction: column;
		> div {
			margin-top: 10px;
			border-radius: 6px;
			height: 100%;
		}
	}
	> section:last-child > div {
		border: 1px solid #aeaeae;
	}
	.search_test {
		height: 100px;
		justify-content: center;
	}
	.test_list {
		height: 100%;
	}
}

.search_field {
	display: grid;
	grid-template-columns: 1.5fr 0.5fr;
	width: 588px;
	gap: 24px;
}

.search_block {
	display: grid;
	grid-template-columns: 4fr 1fr;
}

.header_table {
	display: grid;
	grid-template-columns: repeat(3, 1fr);
	> div {
		border-right: 1px solid #aeaeae;
		border-bottom: 1px solid #aeaeae;
		height: 30px;
	}
	> div:last-child {
		border-right: none;
	}
}

.body_table {
	display: grid;
	grid-template-columns: repeat(3, 1fr);
	> div {
		border-right: 1px solid #aeaeae;
		border-bottom: 1px solid #aeaeae;
		height: 30px;
	}
}

@media screen and (max-width: 1900px) {
	header {
		padding: 0 353px;
	}
}
</style>
