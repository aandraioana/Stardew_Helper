<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>Stardew Helper Dashboard</h1>
    <p>Welcome to the Stardew Helper Dashboard project! This repository contains a Tableau dashboard designed to help you organize crops in each season and maximize profits (daily/per season) in Stardew Valley and also maximize energy/health intake. The data used in this project was sourced from Kaggle, updated with the new crops added in version 1.6 of the game, and written by me from the official Stardew wiki. The project involves data cleaning, joining tables, updating the data, creating formulas for daily/per season profit and visualizing it in an interactive Tableau dashboard.</p>
   <ul> 
       <li><a href="https://public.tableau.com/app/profile/andra.ioana.iuga/viz/Stardew_dashboard/Dashboard1">Stardew Helper Dashboard on Tableau Public</a></li>
   </ul>
    <h2>Table of Contents</h2>
    <ul>
        <li><a href="#overview">Overview</a></li>
        <li><a href="#data-source">Data Source</a></li>
        <li><a href="#data-cleaning-and-preparation">Data Cleaning and Preparation</a></li>
        <li><a href="#new-crops-in-version-16">New Crops in Version 1.6</a></li>
        <li><a href="#tableau-dashboard">Tableau Dashboard</a></li>
        <li><a href="#how-to-use-the-dashboard">How to Use the Dashboard</a></li>
        <li><a href="#getting-started">Getting Started</a></li>
        <li><a href="#contributing">Contributing</a></li>
        <li><a href="#acknowledgements">Acknowledgements</a></li>
    </ul>
    <h2 id="overview">Overview</h2>
    <p>Stardew Valley is a popular farming simulation game where players grow crops, raise animals, and manage their farm. This dashboard helps players optimize their crop choices to maximize profits by providing a detailed analysis of various crops and their profitability, health and energy intake.</p>
    <h2 id="data-source">Data Source</h2>
    <p>The raw data used for this project was sourced from Kaggle:</p>
    <ul>
        <li><a href="https://www.kaggle.com/datasets/shinomikel/stardew-valley-spring-crop-info">Stardew Valley Crop Data on Kaggle</a></li>
    </ul>
    <h2 id="data-cleaning-and-preparation">Data Cleaning and Preparation</h2>
    <p>The following steps were undertaken to clean and prepare the data:</p>
    <ol>
        <li><strong>Keeping only important columns:</strong> Ensured there were no unnecessary info in the dataset by keeping only populated columns.</li>
        <li><strong>Handled missing values:</strong> Filled in or removed any missing data points.</li>
        <li><strong>Standardized formats:</strong> Ensured consistency in data formats (e.g., date formats, text casing).</li>
        <li><strong>Joined tables:</strong> Combined related tables to create a comprehensive dataset.</li>
    </ol>
    <h2 id="new-crops-in-version-16">New Crops in Version 1.6</h2>
    <p>The dataset was updated to include new crops introduced in Stardew Valley version 1.6. This involved:</p>
    <ul>
        <li>Adding new crop data</li>
        <li>Updating existing records to reflect updated game mechanics (different values for health/energy) and crop characteristics</li>
    </ul>
    <h2 id="tableau-dashboard">Tableau Dashboard</h2>
    <p>The Tableau dashboard provides an interactive and user-friendly interface to explore crop data. Key features include:</p>
    <ul>
        <li><strong>Profitability Analysis:</strong> Visualizations showing the profitability of different crops.</li>
        <li><strong>Seasonal Recommendations:</strong> Insights on the best crops to plant in each season.</li>
        <li><strong>Cost-Benefit Analysis:</strong> Detailed breakdown of costs, profits, and time required for each crop.</li>
        <li><strong>Health/Energy Analysis:</strong> Best crop to eat based on energy/health benefits.</li>
    </ul>
    <h2 id="how-to-use-the-dashboard">How to Use the Dashboard</h2>
    <ol>
        <li><strong>Open the Dashboard:</strong> Access the Tableau dashboard through the provided link or file.</li>
        <li><strong>Navigate the Views:</strong> Use the interactive filters and charts to explore crop data.</li>
        <li><strong>Analyze Crops:</strong> Compare different crops based on profitability, season, energy, and other factors.</li>
        <li><strong>Plan Your Farm:</strong> Use the insights to make informed decisions about which crops to plant for maximum profit.</li>
    </ol>
    <h2 id="getting-started">Getting Started</h2>
    <p>To get started with the project, follow these steps:</p>
    <ol>
        <li><strong>Clone the repository:</strong></li>
        <pre><code>git clone https://github.com/yourusername/stardew-valley-crops-dashboard.git</code></pre>
        <li><strong>Open the Tableau workbook:</strong> Open the <code>.twb</code> or <code>.twbx</code> file in Tableau Desktop.</li>
        <li><strong>Explore the Data:</strong> Examine the data and visualizations in Tableau.</li>
    </ol>
    <h2 id="contributing">Contributing</h2>
    <p>Contributions are welcome! If you'd like to contribute to this project, please follow these steps:</p>
    <ol>
        <li><strong>Fork the repository</strong></li>
        <li><strong>Create a new branch:</strong></li>
        <pre><code>git checkout -b feature/your-feature-name</code></pre>
        <li><strong>Make your changes</strong></li>
        <li><strong>Commit your changes:</strong></li>
        <pre><code>git commit -m 'Add some feature'</code></pre>
        <li><strong>Push to the branch:</strong></li>
        <pre><code>git push origin feature/your-feature-name</code></pre>
        <li><strong>Create a pull request</strong></li>
    </ol>
    <h2 id="acknowledgements">Acknowledgements</h2>
    <ul>
        <li><a href="https://www.kaggle.com">Kaggle</a> for the raw Stardew Valley crop data.</li>
        <li>The Stardew Valley community for their ongoing support and contributions to the game on Stardew Wiki and above.</li>
    </ul>
    <p>Feel free to explore the dashboard and make the most out of your Stardew Valley farming experience! If you have any questions or feedback, please open an issue or contact the repository owner.</p>
    <p>Happy farming! 🌾🚜</p>
</body>
</html>
