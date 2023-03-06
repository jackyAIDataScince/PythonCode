import plotly.express as px

data = px.data.tips()
figure = px.sunburst(data, path=["day", "sex"], values="total_bill")
figure.show()

#A sunburst plot is a very popular data visualization technique used to visualize hierarchical data #
# where each level of the hierarchy is represented by a ring or circle where the innermost #circle or ring is the highest level of the hierarchy#.
#Sunburst charts are best to be used when analyzing a dataset where the output #of a variable can be split into multiple factors.
