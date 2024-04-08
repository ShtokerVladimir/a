<template>
	<ConfirmDialog
		:breakpoints="{ '1400px': '75vw', '960px': '75vw', '640px': '100vw' }"
		:style="{ width: '250px !important', padding: '20px' }"
		group="headless"
	>
		<template #container="{ message, acceptCallback }">
			<p>
				{{ message.message }}
			</p>
			<form @submit.prevent="acceptCallback()">
				<InputOtp v-model="emailCode">
					<template #default="{ attrs, events }">
						<input
							v-bind="attrs"
							v-on="events"
							type="text"
							class="custom-otp-input"
						/>
					</template>
				</InputOtp>
				<ButtonComponent
					type="submit"
					label="Подтвердить"
					:disabled="emailCode === ''"
				/>
			</form>
		</template>
	</ConfirmDialog>
	<Toast />
</template>
<script setup lang="ts">
import ConfirmDialog from 'primevue/confirmdialog'
import InputOtp from 'primevue/inputotp'
import Toast from 'primevue/toast'
import { useConfirm } from 'primevue/useconfirm'
import { useToast } from 'primevue/usetoast'
import { onMounted, ref } from 'vue'
import ButtonComponent from './ButtonComponent.vue'

const confirm = useConfirm()
const toast = useToast()
const emailCode = ref()

const showConfirm = () => {
	confirm.require({
		group: 'headless',
		message:
			'Подтвердите свой адрес электронной почты, код подтверждения будет отправлен на вашу почту.',
		icon: 'pi pi-info-circle',
		header: 'Confirmation',
		accept: () => {
			toast.add({
				severity: 'success',
				summary: 'Confirmed',
				detail: 'Successfully confirmed',
				life: 3000,
			})
		},
		reject: () => {
			toast.add({
				severity: 'error',
				summary: 'Rejected',
				detail: 'You have rejected',
			})
		},
	})
}

onMounted(() => {
	showConfirm()
})
</script>
<style scoped>
.custom-otp-input {
	width: 100%;
	font-size: 36px;
	border: 0 none;
	appearance: none;
	color: #000000;
	text-align: center;
	transition: all 0.2s;
	background: transparent;
	border-bottom: 2px solid #aeaeae;
}

.custom-otp-input:focus {
	outline: 0 none;
	border-bottom-color: var(--primary-color);
}

form {
	margin-top: 30px;
	text-align: center;
	display: flex;
	flex-direction: column;
	gap: 20px;
	> button {
	}
}
</style>
