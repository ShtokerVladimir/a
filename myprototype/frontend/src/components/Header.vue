<script setup lang="ts"></script>
<template>
	<header>
		<ol>
			<li>
				<span class="pi pi-fw pi-home"></span
				><RouterLink to="/">Главная</RouterLink>
			</li>
			<li>
				<span class="pi pi-fw pi-plus"></span
				><RouterLink to="/new-test">Новое тестирование</RouterLink>
			</li>
			<li>
				<span class="pi pi-fw pi-bars"></span
				><RouterLink to="/last-test">Последние тестирования</RouterLink>
			</li>
			<li>
				<span class="pi pi-fw pi-list"></span
				><RouterLink to="/all-test">Тесты</RouterLink>
			</li>
		</ol>
	</header>
</template>
<style scoped>
header {
	display: flex;
	justify-content: space-between;
	align-items: center;
	width: 100%;
	height: 60px;
	background-color: #d9d9d9;
	padding: 0 360px;
}

a {
	font-size: 20px;
	line-height: 29.05px;
}

ol {
	display: grid;
	grid-template-columns: 6fr repeat(2, 3fr) 1.3fr;
	align-items: center;
	padding: 0;
	margin: 0;
}

ol > li {
	display: flex;
	align-items: center;
	gap: 2px;
	> span {
		font-size: 20px;
		padding-top: 1px;
	}
}

ol > li:nth-last-child(1) {
	justify-self: end;
}
ol > li:nth-last-child(2) {
	justify-self: center;
}
ol > li:nth-last-child(3) {
	justify-self: start;
}

li {
	display: flex;
	align-items: center;
	gap: 2px;
}

@media screen and (max-width: 1200px) {
	header {
		padding: 0 300px;
	}
}

@media screen and (max-width: 1000px) {
	header {
		padding: 0 200px;
	}
}

@media screen and (max-width: 800px) {
	header {
		padding: 0 100px;
	}
}

@media screen and (max-width: 600px) {
	header {
		padding: 0 50px;
	}
}

@media screen and (max-width: 400px) {
	header {
		padding: 0 20px;
	}
}
</style>
