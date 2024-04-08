<script setup lang="ts">
import Button from 'primevue/button'
import InputText from 'primevue/inputtext'
import Header from '../components/Header.vue'
</script>

<template>
	<Header />
	<main>
		<section class="search_test">
			<h1>Поиск</h1>
			<div>
				<InputText type="text" />
				<Button label="Поиск" @click="() => {}" />
				<Button label="Создать новый тест" @click="() => {}" />
			</div>
		</section>
		<section class="test_list">
			<h1>Тесты</h1>
			<div>Тесты</div>
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
	}
	.test_list {
		height: 100%;
	}
}
</style>
