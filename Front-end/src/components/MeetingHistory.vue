<template>
	<el-table
		:data="tableData"
		style="width: 100%"
		max-height="500">
	<el-table-column type="expand">
		<template slot-scope="props">
			<el-form :inline="true" :model="formInline" label-position="left" class="demo-table-expand">
				<el-form-item label="Name">
					<span>{{ props.row.name }}</span>
				</el-form-item>
				<el-form-item label="Date">
					<span>{{ props.row.date }}</span>
				</el-form-item>
				<el-form-item label="Time Slot">
					<span>{{ props.row.time }}</span>
				</el-form-item>
				<el-form-item label="Site">
					<span>{{ props.row.site }}</span>
				</el-form-item>
				<el-form-item label="Location">
					<span>{{ props.row.location }}</span>
				</el-form-item>
				<el-form-item label="Initiator">
					<span>{{ props.row.initiator }}</span>
				</el-form-item>
				<el-form-item label="Number">
					<span>{{ props.row.attendee_number }}</span>
				</el-form-item>
				<el-form-item label="Attendees">
					<span>{{ props.row.attendees }}</span>
				</el-form-item>
				<el-form-item label="Files">
					<span>{{ props.row.files }}</span>
				</el-form-item>
				<el-form-item label="Record">
					<span>{{ props.row.record }}</span>
				</el-form-item>
			</el-form>
		</template>
	</el-table-column>
	<el-table-column
		fixed
		prop="date"
		label="Date"
		width="100">
	</el-table-column>
	<el-table-column
		fixed
		prop="name"
		label="Name"
		width="150">
	</el-table-column>
	<el-table-column
		fixed
		prop="site"
		label="Site"
		width="70">
	</el-table-column>
	<el-table-column
		fixed
		prop="location"
		label="Location"
		width="100">
	</el-table-column>
	<el-table-column
		fixed
		prop="attendee_number"
		label="Number"
		width="100">
	</el-table-column>
	<el-table-column
		fixed
		prop="initiator"
		label="Initiator">
	</el-table-column>
	<el-pagination
		background
		small
		layout="prev, pager, next"
		:total="50">
	</el-pagination>
	</el-table>
</template>

<script>
	export default {
		data() {
			return {
				tableData: [{
				date: '2019/07/11',
				name: 'test meeting',
				site: 'test',
				location: 'test',
				attendee_number: 3,
				initiator: 'AAA',
				attendees: 'AAA BBB CCC',
				files: '*******',
				record: '*********************************\n',
				time: '9:30 - 11:00'
				},
				{date: '2019/07/10',
				name: 'Weekly meeting',
				site: 'A',
				location: 'R105',
				attendee_number: 10,
				initiator: 'AAA',
				attendees: 'AAA BBB CCC DDD EEE FFF GGG HHH III JJJ KKK',
				files: 'record.txt\nmain.cpp\n',
				record: '*********************************\n',
				time: '8:30 - 10:00'
				},
				{date: '2019/07/10',
				name: 'ID003',
				site: 'A',
				location: 'R104',
				attendee_number: 5,
				initiator: 'L',
				attendees: 'X Y Z O L',
				files: 'no',
				record: '*********************************\n',
				time: '13:30 - 15:00'
				},
				{date: '2019/07/08',
				name: 'ID002',
				site: 'F, D',
				location: 'F-R303, D-R102',
				attendee_number: 7,
				initiator: 'ABC',
				attendees: 'F: ABC, ABB, AAB, AABB\nD:QWER, TYUI, ASDF',
				files: 'record.txt\nmain.cpp\n',
				record: '*********************************\n',
				time: '8:30 - 10:00'
				}]
			}
		}
	}
</script>

<style>
	.demo-table-expand {
		font-size: 0;
	}
	.demo-table-expand label {
	width: 90px;
	color: #99a9bf;
	}
	.demo-table-expand .el-form-item {
	margin-right: 0;
	margin-bottom: 0;
	width: 80%;
	}
</style>
