<template>
  <div id="parent">
    <div class="header">
      <div class="left">
        <el-button-group>
          <el-button type="primary" size="mini" @click="prev">&lt;</el-button>
          <el-button type="primary" size="mini" @click="next">&gt;</el-button>
        </el-button-group>
        &nbsp;&nbsp;&nbsp;{{headerContent}}
      </div>
      <div class="right">
        <el-button-group>
          <el-button type="primary" size="mini" @click="switchMonth">month</el-button>
          <el-button type="primary" size="mini" @click="switchWeek">week</el-button>
        </el-button-group>
      </div>
    </div>
    <div class="body">
      <table class="month-table"  cellspacing="0" cellpadding="0" v-show="showMonth">
        <thead>
          <th>Mon</th>
          <th>Tue</th>
          <th>Wed</th>
          <th>Thu</th>
          <th>Fri</th>
          <th>Sat</th>
          <th>Sun</th>
        </thead>
        <tbody>
          <tr v-for="(week, weekIndex) in dates" v-bind:key="weekIndex">
            <td v-for="(date, dateIndex) in dates[weekIndex]"
              v-bind:key="dateIndex"
              @mouseenter="dateMouseEnter(weekIndex, dateIndex)"
              @mouseleave="dateMouseLeave(weekIndex, dateIndex)">
              <div
              class="date"
              :class="[date.class, date.isAlive]">
                <h4>{{date.day}}</h4>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
      <table class="week-table"  cellspacing="0" cellpadding="0" v-show="!showMonth">
        <thead>
          <th></th>
          <th v-for="(header, index) in weekTableHeader" v-bind:key="index" :class="header.class">{{header.date}}</th>
        </thead>
        <tbody>
          <tr v-for="(content, index) in weekList" v-bind:key="index">
            <td>
              <div class="hours">
                <span>{{content.time}}</span>
              </div>
            </td>
            <td>
              <div v-for="(item, slot) in weekList[index].mon" v-bind:key="slot" @click="detail(index, slot, 1)">
                <div :class="[item==0?class1:class2]">
                  &nbsp{{meeting[0][index][slot].meeting_info}}
                </div>
              </div>
            </td>
            <td>
              <div v-for="(item, slot) in weekList[index].tue" v-bind:key="slot" @click="detail(index, slot, 2)">
                <div :class="[item==0?class1:class2]">
                  &nbsp{{meeting[1][index][slot].meeting_info}}
                </div>
              </div>
            </td>
            <td>
              <div v-for="(item, slot) in weekList[index].wed" v-bind:key="slot" @click="detail(index, slot, 3)">
                <div :class="[item==0?class1:class2]">
                  &nbsp{{meeting[2][index][slot].meeting_info}}
                </div>
              </div>
            </td>
            <td>
              <div v-for="(item, slot) in weekList[index].thu" v-bind:key="slot" @click="detail(index, slot, 4)">
                <div :class="[item==0?class1:class2]">
                  &nbsp{{meeting[3][index][slot].meeting_info}}
                </div>
              </div>
            </td>
            <td>
              <div v-for="(item, slot) in weekList[index].fri" v-bind:key="slot" @click="detail(index, slot, 5)">
                <div :class="[item==0?class1:class2]">
                  &nbsp{{meeting[4][index][slot].meeting_info}}
                </div>
              </div>
            </td>
            <td>
              <div v-for="(item, slot) in weekList[index].sat" v-bind:key="slot" @click="detail(index, slot, 6)">
                <div :class="[item==0?class1:class2]">
                  &nbsp{{meeting[5][index][slot].meeting_info}}
                </div>
              </div>
            </td>
            <td>
              <div v-for="(item, slot) in weekList[index].sun" v-bind:key="slot" @click="detail(index, slot, 7)">
                <div :class="[item==0?class1:class2]">
                  &nbsp{{meeting[6][index][slot].meeting_info}}
                </div>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import moment from 'moment'
export default {
  data () {
    return {
      class1: 'class1',
      class2: 'class2',
      today: moment().format('YYYY-MM-DD'),
      currentYearMonth: moment().format('YYYY-MM'),
      weekTableHeader: [],
      dates: [],
      showMonth: false,
      weekList: [],
      headerContent: moment().format('MM/DD')+'~'+moment().add(6,'days').format('MM/DD'),
      currentWeekday: '',
      meeting: []
    }
  },
  methods: {
    // 点击上个月 通过改变currentYearMonth来获取上个月的 YYYY-MM 格式
    prev () {
      if (this.showMonth) {
        this.currentYearMonth = moment(this.currentYearMonth).subtract(1, 'months').format('YYYY-MM')
        this.headerContent = this.currentYearMonth
        this.createCalendar()
      } else {
        this.currentWeekday = moment(this.currentWeekday).subtract(7, 'days')
        this.weekHeaderContent()
        this.createWeekList()
      }
      console.log(this.headerContent)
    },
    detail(index, slot, day){
      if (this.meeting[day-1][index][slot].meeting_id != '0') alert()
    },
    next () {
      if (this.showMonth) {
        this.currentYearMonth = moment(this.currentYearMonth).add(1, 'months').format('YYYY-MM')
        this.headerContent = this.currentYearMonth
        this.createCalendar()
      } else {
        this.currentWeekday = moment(this.currentWeekday).add(7, 'days')
        this.weekHeaderContent()
        this.createWeekList()
      }
        console.log(this.headerContent)

    },
    switchMonth () {
      this.showMonth = true
      this.headerContent = this.currentYearMonth
    },
    switchWeek () {
      this.showMonth = false
      this.weekHeaderContent()
    },
    dateMouseEnter (weekIndex, dateIndex) {
      this.dates[weekIndex][dateIndex].isAlive = 'date-alive'
    },
    dateMouseLeave (weekIndex, dateIndex) {
      this.dates[weekIndex][dateIndex].isAlive = ''
    },
    createCalendar () {
      this.dates = []
      // 获取当月的一号是星期几 以便来生成上月的日期 填补够42个格子
      const monthFirstDay = moment(this.currentYearMonth + '-01', 'YYYY-MM-DD')
      // 获得一号与第一个格子内应该有的天数距离 这里需要注意的是 weekday 是从周日 为 0 开始的
      let firstDayWeekday = moment(monthFirstDay).weekday()
      if (firstDayWeekday === 0) {
        firstDayWeekday = 7
      }
      let daysDistance = 1 - firstDayWeekday
      for (let weeks = 0; weeks < 6; weeks++) {
        this.dates.push([])
        for (let weekday = 0; weekday < 7; weekday++) {
          // 该对象有两个属性 一个是class属性 还有一个就是日期
          let date = {}
          date.day = moment(monthFirstDay).add(daysDistance, 'days')
          date.isAlive = ''
          const dayMonth = moment(date.day).month()
          // 是这个月的日期
          if (dayMonth === moment(monthFirstDay).month()) {
            date.class = 'current-month '
            // 日期是今天的高亮
            if (moment(date.day).isSame(this.today, 'days')) {
              date.class += 'today '
            }
          } else {
            date.class = 'not-current-month '
          }
          date.day = moment(date.day).format('DD')
          this.dates[weeks].push(date)
          daysDistance++
        }
      }
    },
    createWeekList () {
      this.weekTableHeader = ['Mon ', 'Tue ', 'Wed ', 'Thu ', 'Fri ', 'Sat ', 'Sun ']
      this.weekList = []
      for (let index = 0; index < 7; index++) {
        let item = {}
        item.date = moment(this.currentWeekday).add(index, 'days')
        if (item.date.isSame(this.today, 'days')) {
          item.class = 'today'
        }
        item.date = this.weekTableHeader[index] + item.date.format('MM/DD')
        this.weekTableHeader[index] = item
      }
        for (let hours = 0; hours < 24; hours++) {
          let item = {}
          item.time = hours + ':00'
          item.mon = [0, 0, 0, 0]
          item.tue = [0, 0, 0, 0]
          item.wed = [0, 0, 0, 0]
          item.thu = [0, 0, 0, 0]
          item.fri = [0, 0, 0, 0]
          item.sat = [0, 0, 0, 0]
          item.sun = [0, 0, 0, 0]
          this.weekList.push(item)
      }
      for (let day = 0; day < 7; day++) {
        this.meeting.push([])
        for (let time = 0; time < 24; time++) {
          this.meeting[day].push([])
          for (let slot = 0; slot <4; slot++) {
            let item = {}
            item.meeting_id = '0'
            item.meeting_info = ' '
            this.meeting[day][time].push(item)
          }
        }
      }
      this.weekList[10].mon[2] = 1
      this.weekList[10].mon[3] = 1
      this.meeting[0][10][2].meeting_info = 'Meeting1 @Room2'
      this.meeting[0][10][3].meeting_info = 'Meeting1 @Room2'
      this.meeting[0][10][2].meeting_id = '1'
      this.meeting[0][10][3].meeting_id = '1'
      this.weekList[15].wed[0] = 1
      this.weekList[15].wed[1] = 1
      this.weekList[15].wed[2] = 1
      this.weekList[15].wed[3] = 1
      this.meeting[2][15][0].meeting_info = 'Meeting2 @Room1'
      this.meeting[2][15][1].meeting_info = 'Meeting2 @Room1'
      this.meeting[2][15][2].meeting_info = 'Meeting2 @Room1'
      this.meeting[2][15][3].meeting_info = 'Meeting2 @Room1'
      this.meeting[2][15][0].meeting_id = '2'
      this.meeting[2][15][1].meeting_id = '2'
      this.meeting[2][15][2].meeting_id = '2'
      this.meeting[2][15][3].meeting_id = '2'
    },
    weekHeaderContent () {
      this.headerContent = moment(this.currentWeekday).format('MM/DD') + '~' + moment(this.currentWeekday).add(6, 'days').format('MM/DD')
    }
  },
  created () {
    // v-show是在创建后 保留dom 只是做切换的 不会v-if那样 销毁dom 所以只需要创建一次
    this.createCalendar()
    let weekday = moment().weekday() === 0 ? 7 : moment().weekday()
    let daysDistance = 1 - weekday
    this.currentWeekday = moment().add(daysDistance, 'days')
    this.createWeekList()
      console.log(this.headerContent)
  }
}
</script>

<style lang="less" scoped>
#parent {
  margin: 2rem auto;
  padding: 1rem;
  border: 1px solid #ebeef5;
}
.header {
  display: flex;
  justify-content: space-between;
  padding: 12px 20px;
  font-size: 18px;
  border-bottom: 1px solid #ebeef5;
}
.body {
  padding: 12px 20px 35px;
}
table {
  table-layout: fixed;
  width: 100%;
}
table thead th {
  padding: 10px 0;
  font-weight: 400;
}
tbody tr {
  display: table-row;
  vertical-align: inherit;
  border-color: inherit;
}
.month-table tbody td {
  vertical-align: inherit;
  border-right: 1px solid #ebeef5;
  border-bottom: 1px solid #ebeef5;
}
.month-table tbody tr:first-child td {
  border-top: 1px solid #ebeef5;
}
.month-table tr td:first-child {
  border-left: 1px solid #ebeef5;
}
.date {
  box-sizing: border-box;
  padding: 8px;
  height: 84px;
}
.not-current-month {
  color: #909399;
}
.current-month {
  color: #000000;
}
.today {
  color: #F44E50;
  background-color: #FFFF99;
}
.date-alive {
  background-color: rgb(252, 212, 215);
}
.week-table tbody tr td {
  border: 1px solid #ebeef5;
}
.hours{
  text-align: center;
  height: 80px;
}
.class1{
  text-align: center;
  margin: 0px;
}
.class2{
  text-align: center;
  margin: 0px;
  cursor: pointer;
}
h5{
  margin: -3px;
}
h4{
  margin: 8px;
}
</style>
