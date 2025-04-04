<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Recipe Finder</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <header>
            <h1>Recipe Finder</h1>
        </header>
        <main>
            <section class="background-video">
                <video autoplay loop muted>
                    <source src="assets/food-background.mp4" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
            </section>
            <section class="search">
                <input type="text" id="ingredientInput" placeholder="Enter ingredients...">
                <button onclick="searchRecipes()">Search</button>
            </section>
            <section id="results">
                <!-- Receipe results will be displayed here -->
            </section>
        </main>
        <script src="script.js"></script>
    </body>
    </html>

    body {
        margin: 0;
        font-family: Arial, sans-serif;
        text-align: center;
        color:white;
    }
    
    .background-video{
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        overflow: hidden;
        z-index: -1;
    }

    .background-video video {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }


    header {
        position: relative;
        padding: 20px;
        font-size: 2em;
        background: rgba(0, 0, 0, 0.5);
    }

    .search {
        position: relative;
        margin-top: 50px;
        background: rgba(0, 0, 0, 0.6);
        padding: 20px;
        border-radius: 10px;
        display: inline-block;
    }

    imput {
        padding: 10px;
        width: 250px;
        border: none;
        border-radius: 5px;
    }

    button {
        padding: 10px 20px;
        background: #ff6600;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer:
    }

    #results {
        margin-top: 30px;
        background: rgba(0, 0, 0, 0.5);
        padding: 20px;
        border-radius: 10px;
        display: inline-block;
        width: 80%;
    }