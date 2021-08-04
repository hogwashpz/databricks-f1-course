# Databricks notebook source
dbutils.widgets.text("input", "", "Send the parametar value")

# COMMAND ----------

input_param = dbutils.widgets.get("input")

# COMMAND ----------

print("I am the child notebook: " + input_param)

# COMMAND ----------

dbutils.notebook.exit(100)
