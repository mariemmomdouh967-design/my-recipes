from flask import Flask, jsonify, render_template # type: ignore

app = Flask(__name__, static_url_path='/static', static_folder='static')

# Recipes data (15 items)
recipes = [
    {
        "name": "Stuffed Pies with Meat",
        "image_url": "/static/img/fb.jpg",
        "ingredients": ["Pie dough or phyllo sheets", "Ground meat", "Chopped onion", "Olive oil or butter", "Salt, pepper, spices to taste", "Egg + milk (for brushing)" ],
        "steps": [
            "Cook the onion and meat with spices",
            "Layer the dough sheets in a pan, brushing each with oil or butter, and spread the filling on top.",
            "Cover with remaining dough layers and brush with egg-milk mixture.",
            "Bake at 180°C (350°F) until golden and crispy, about 30–45 minutes, then cut and serve warm."
        ]
    },
    {
        "name": "Herb-Roasted Beef",
        "image_url": "/static/img/cb.jpg",
        "ingredients": ["Beef roast", "Garlic cloves, minced", "Fresh thyme and rosemary", "Olive oil", "Salt and black pepper"],
        "steps": [
            "Rub the beef with olive oil, garlic, herbs, salt, and pepper.",
            "Sear in a hot pan until browned on all sides.",
            "Transfer to oven and roast at 180°C (350°F) until desired doneness.",
            "Rest for 10 minutes, slice, and serve with sides like potatoes or vegetables."
        ]
    },
    {
        "name": "Ebi Katsu Burger",
        "image_url": "/static/img/d.jpg",
        "ingredients": ["Chopped shrimp", "Flour, egg, panko", "Lettuce, tomato", "Mozzarella cheese", "Brioche buns", "Mayonnaise-based sauce"],
        "steps": [
            "Mix shrimp with seasonings and form patties.",
            "Coat patties with flour, egg, and panko.",
            "Fry until golden and crispy.",
            "Assemble burger with lettuce, tomato, cheese, patty, and sauce in buns."
         ]   
    },
    {
       "name": "Penne alla Vodka",
        "image_url": "/static/img/8.jpg",
        "ingredients": ["Penne pasta", "Tomato sauce", "Heavy cream", "Pancetta or cooked meat (optional)", "Vodka, Olive oil, Salt and pepper", "Fresh basil and grated cheese"],
        "steps": [
           "Cook penne pasta according to package instructions.",
            "In a pan, sauté onion/garlic and pancetta (if using) in olive oil.",
            "Add tomato sauce, cream, and a splash of vodka; simmer until creamy and slightly thickened.",
            "Toss cooked pasta in the sauce, season with salt and pepper, and serve garnished with basil."
         ]   
    },
    {
        "name":"Baked Lasagna",
        "image_url": "/static/img/55f.jpg",
        "ingredients": ["Lasagna noodles", "Tomato sauce", "Ground meat or vegetables", "Mozzarella, ricotta, and Parmesan cheese", "Olive oil, Salt and pepper "],
        "steps": [
           "Preheat oven to 180°C (350°F).",
            "Cook noodles according to package instructions.",
            "Layer noodles, sauce, meat/vegetables, and cheeses in a baking dish.",
            "Repeat layers, finishing with cheese on top.",
            "Bake until cheese is golden and bubbling, about 30–45 minutes.",
            "Let rest a few minutes, then slice and serve."
         ]   
    },
    {
        "name":"Mini Pancakes",
        "image_url": "/static/img/00.jpg",
        "ingredients": ["Flour", "Eggs", "Milk", "Baking powder", "Sugar", "Vanilla extract", "Toppings: caramel, chocolate sauce, honey, or maple syrup"],
        "steps": [
           "Mix flour, baking powder, sugar, eggs, milk, and vanilla until smooth.",
            "Heat a non-stick pan and pour small amounts of batter to form mini pancakes.",
            "Cook until bubbles form on top, then flip and cook until golden.",
            "Serve with blueberries and desired toppings like syrup, chocolate, or carame."
        ]
    },
    {
       "name":"Ice Cream Crepe",
        "image_url": "/static/img/c.jpg",
        "ingredients": ["Crepe batter (flour, eggs, milk, sugar, butter)", "Chocolate sauce or melted chocolate", "Ice cream (flavor of choice)", "Optional toppings: whipped cream, fruits, nuts"],
        "steps": [
           "Prepare the crepe batter and cook thin crepes in a non-stick pan.",
            "Spread chocolate sauce on the crepe and add a scoop of ice cream.",
            "Fold or roll the crepe, then top with optional whipped cream, fruits, or nuts.",
            "Serve immediately and enjoy."
    ]
    },
    {
  "name":"Lotus Biscoff Cheesecake",
        "image_url": "/static/img/7.jpg",
        "ingredients": ["Cream cheese", "Sugar, Eggs", "Vanilla extract", "Lotus Biscoff cookies (for crust and decoration)", "Butter (for crust)"],
        "steps": [
           "Crush Lotus Biscoff cookies and mix with melted butter to form the crust; press into a springform pan.",
            "Beat cream cheese, sugar, eggs, and vanilla until smooth, then pour over the crust.",
            "Bake at 160°C (320°F) until set, then cool and refrigerate.",
            "Decorate with whole or crushed Lotus cookies and drizzle with Biscoff spread before serving."
    ]
    },
    {
        "name":"Chocolate Swiss Roll",
        "image_url": "/static/img/kk.jpg",
        "ingredients": ["Flour", "Sugar, Eggs", "Cocoa powder", "Baking powder", "Butter", "Chocolate ganache or whipped cream (for filling)"],
        "steps": [
           "Beat eggs and sugar until fluffy, then fold in flour, cocoa powder, and baking powder.",
            "Spread batter on a baking tray and bake until just set; let cool slightly.",
            "Spread chocolate ganache or whipped cream over the sponge, then roll tightly.",
            "Chill if desired, slice, and serve.."
    ] 
    },
    {
        "name":"Crème Caramel",
        "image_url": "/static/img/1338.jpg",
        "ingredients": ["Milk or cream", "Eggs", "Sugar", "Vanilla extract", "Sugar (for caramel)",],
        "steps": [
           "Make caramel by melting sugar until golden and pour into serving molds.",
            "Mix eggs, sugar, milk, and vanilla until smooth, then pour over the caramel.",
            "Bake in a water bath until set, then cool and refrigerate.",
            "Unmold and serve chilled."
    ] 
    },
    {
        "name":"Cheese Pizza",
        "image_url": "/static/img/pizza.jpg",
        "ingredients": ["Pizza dough", "Tomato sauce", "Mozzarella cheese (or mix of cheeses)", "Olive oil", "Optional: herbs like oregano or basil",],
        "steps": [
           "Preheat oven to 220°C (425°F).",
            "Spread tomato sauce over the rolled-out dough and top with cheese and herbs.",
            "Bake until crust is golden and cheese is melted, about 12–15 minutes..",
            "Slice and serve hot."
    ] 
    },
    {
        "name":"Chicken Salad",
        "image_url": "/static/img/a.jpg",
        "ingredients": ["Cooked chicken, chopped (grilled or boiled)", "Leafy greens (lettuce or mixed greens)", "Boiled eggs, sliced", "Cherry tomatoes or chopped tomatoes",],
        "steps": [
           "Arrange leafy greens as a base in a bowl or plate.",
           "Add chopped chicken, sliced boiled eggs, and tomatoes on top..",
           "Drizzle with dressing and toss gently to combine..",
           "Serve immediately as a main dish or side.."
    ] 
    },
    {
       "name":"Butter Chicken",
        "image_url": "/static/img/7bd.jpg",
        "ingredients": ["Chicken", "Butter", "Tomato puree", "Cream, Salt", "Indian spices, Naan or rice",],
        "steps": [
           "Cook marinated chicken until lightly browned.",
            "Prepare a creamy tomato-butter sauce with spices and simmer until thickened.",
            "Add chicken to the sauce and cook until fully coated and tender.",
            "Garnish with cilantro and serve hot with naan or rice."
    ] 
    },
    {
          "name":"Swedish Meatballs",
        "image_url": "/static/img/dd386.jpg",
        "ingredients": ["Ground beef", "Onion, finely chopped", "Bread crumbs, Egg", "Salt and pepper", "Cream (for sauce), Butter",],
        "steps": [
           "Mix ground meat with onion, bread crumbs, egg, salt, and pepper; form into small balls.",
            "Fry meatballs in butter or oil until browned and cooked through.",
            "Prepare cream sauce in the same pan, then add meatballs to coat.",
            "Serve with mashed potatoes, broccoli, and lingonberry jam or pickles." 
    ]  
    },
    {
          "name":"Patty Melt",
        "image_url": "/static/img/6cf8.jpg",
        "ingredients": ["Ground beef patty", "Swiss cheese", "Caramelized onions", "Rye bread slices", "Butter",],
        "steps": [
           "Cook ground beef patty until done.",
            "Caramelize onions in butter.",
            "Assemble patty, cheese, and onions between rye bread slices, butter the outside.",
            "Grill sandwich until bread is golden and cheese is melted."  
    ]  
    },

 ] 
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recipes")
def get_recipes():
    return jsonify(recipes)

if __name__ == "__main__":

    app.run(debug=True)
