import { defineStore } from 'pinia'

const tests = [
	{
		name: 'VipCallPersons',
		code: 'VipCallPersons',
		date: '04/06/2022 18:00',
		result: 'pass',
	},
	{
		name: 'VipCallPersons',
		code: 'VipCallPersons',
		date: '04/06/2022 18:00',
		result: 'pass',
	},
	{
		name: 'VipCallPersons',
		code: 'VipCallPersons',
		date: '04/06/2022 18:00',
		result: 'pass',
	},
	{
		name: 'VipCallPersons',
		code: 'VipCallPersons',
		date: '04/06/2022 18:00',
		result: 'pass',
	},
	{
		name: 'VipCallPersons',
		code: 'VipCallPersons',
		date: '04/06/2022 18:00',
		result: 'pass',
	},
	{
		name: 'VipCallPersons',
		code: 'VipCallPersons',
		date: '04/06/2022 18:00',
		result: 'pass',
	},
	{
		name: 'VipCallPersons',
		code: 'VipCallPersons',
		date: '04/06/2022 18:00',
		result: 'pass',
	},
	{
		name: 'VipCallPersons',
		code: 'VipCallPersons',
		date: '04/06/2022 18:00',
		result: 'pass',
	},
	{
		name: 'VipCallPersons',
		code: 'VipCallPersons',
		date: '04/06/2022 18:00',
		result: 'pass',
	},
	{
		name: 'VipCallPersons',
		code: 'VipCallPersons',
		date: '04/06/2022 18:00',
		result: 'pass',
	},
	{
		name: 'VipCallPersons',
		code: 'VipCallPersons',
		date: '04/06/2022 18:00',
		result: 'pass',
	},
	{
		name: 'VipCallPersons',
		code: 'VipCallPersons',
		date: '04/06/2022 18:00',
		result: 'pass',
	},
	{
		name: 'VipCallPersons',
		code: 'VipCallPersons',
		date: '04/06/2022 18:00',
		result: 'pass',
	},
	{
		name: 'VipCallPersons',
		code: 'VipCallPersons',
		date: '04/06/2022 18:00',
		result: 'pass',
	},
	{
		name: 'VipCallPersons',
		code: 'VipCallPersons',
		date: '04/06/2022 18:00',
		result: 'pass',
	},
	{
		name: 'VipCallPersons',
		code: 'VipCallPersons',
		date: '04/06/2022 18:00',
		result: 'pass',
	},
	{
		name: 'VipCallPersons',
		code: 'VipCallPersons',
		date: '04/06/2022 18:00',
		result: 'pass',
	},
	{
		name: 'VipCallPersons',
		code: 'VipCallPersons',
		date: '04/06/2022 18:00',
		result: 'pass',
	},
	{
		name: 'VipCallPersons',
		code: 'VipCallPersons',
		date: '04/06/2022 18:00',
		result: 'pass',
	},
	{
		name: 'VipCallPersons',
		code: 'VipCallPersons',
		date: '04/06/2022 18:00',
		result: 'pass',
	},
	{
		name: 'VipCallPersons',
		code: 'VipCallPersons',
		date: '04/06/2022 18:00',
		result: 'pass',
	},
	{
		name: 'VipCallPersons',
		code: 'VipCallPersons',
		date: '04/06/2022 18:00',
		result: 'pass',
	},
	{
		name: 'VipCallPersons',
		code: 'VipCallPersons',
		date: '04/06/2022 18:00',
		result: 'pass',
	},
	{
		name: 'VipCallPersons',
		code: 'VipCallPersons',
		date: '04/06/2022 18:00',
		result: 'pass',
	},
	{
		name: 'VipCallPersons',
		code: 'VipCallPersons',
		date: '04/06/2022 18:00',
		result: 'pass',
	},
	{
		name: 'VipCallPersons',
		code: 'VipCallPersons',
		date: '04/06/2022 18:00',
		result: 'pass',
	},
]

export const useTestStore = defineStore('test', {
	actions: {
		getTests() {
			return tests
		},
	},
	state: () => ({
		tests,
	}),
})
