<template>
  <div>
    <div class="row">
      <div class="col-md-6 col-12" v-for="table in overviewData" :key="table.title">
        <card>
            <h4>{{ table.title }}</h4>
            <paper-table :data="table.tableData" :columns="table.tableColumns">
                <template slot="columns">
                    <th>Item</th>
                    <th>Quantity</th>
                </template>
                <template slot-scope="{row}">
                    <td>{{row.item}}</td>
                    <td>{{row.quantity}}</td>
                </template>
            </paper-table>
        </card>
      </div>
    </div>
  </div>
</template>
<script>
import { PaperTable } from "@/components/index";
export default {
  components: {
    PaperTable
  },

  data() {
    return {
      overviewData: [
          {
              title: "Weapons",
              tableColumns: ["Item", "Quantity"],
              tableData: [
                  {
                      item: "Wand",
                      quantity: 2
                  },
                  {
                      item: "Sword",
                      quantity: 1
                  },
                  {
                      item: "Whip",
                      quantity: 5
                  }
              ]
          }
      ],
    };
  }
};
</script>
<style>
</style>
