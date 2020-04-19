# Team Rocket

# Blasting off Again!


Modeling The Future

Forrest Bicker & Eszter Morvay

---



# 1	Introduction


## 1.1	Executive Summary

Contributing almost a trillion (992 billion) dollars to the U.S. economy, the food and agriculture industry is especially important to consider when thinking of the future of the United States. Agriculture is a fundamental societal building block: it has not only an economic importance in addition to providing a source of food, but a wide range of effects on other industries due to the many different uses of crops. The agricultural industry is maintained mostly by small family farms, accounting for about 90% of all farms in the U.S.

However, farming is a very risky business, as the yield is easily affected by fluctuations in uncontrollable natural weather patterns. For this reason, crop insurance is crucial in keeping the industry stable. Farmers are supported by the federal government via a subsidy that covers much of the cost of this insurance, and the federal government on average subsidizes 62% of the premiums. Climate and water availability are crucial factors that help determine the yield of the many different kinds of crops made in the United States, which is why the changing climate presents a great risk to this industry.

In this paper, historic climate data from the NOAA is used to forecast effects of weather on the corn industry in Iowa. Climate data is forecasted using polynomial regression, and the forecasted climate data, along with crop loss and insurance policy information for Iowa’s counties from the USDA is used to make predictions on the frequency, probability, cost, and severity. A neural network takes in the predicted climate data as parameters and is used to predict the severity (the proportion of acres in an indemnity damaged) of expected crop loss. Frequency is modeled by forecasting the number of lost acres in a year, and cost predicts the expected value of the total indemnity payment by year. Data tables and scatter plots are included throughout the paper and in an appendix to show the equations and types of models used for extrapolation and interpolation.

The results suggest that total cost, frequency, probability, and severity will all increase. Probability will only increase marginally, severity will increase considerably, while cost and frequency will experience the most drastic changes. It is expected that cost will see an increase of almost 300% by 2050, leading to a high price for indemnities. All of these factors combined pose a great risk to the Iowa corn farming industry and the many who rely on corn for their livelihood. Corn is a crop that has much greater influence outside of simply its own industry, because of the wide variety of possible uses for corn, especially as ethanol and livestock feed, so any impact to the corn industry will spillover to the related industries. For these reasons, an effective solution would be the government increasing subsidies for corn farmers, so as to keep the industry stable and afloat, and/or the government increasing investment in a sector that is heavily dependent on corn, so as to increase demand and profitability of corn, making sure farmers stay in the business. In the long term, taking steps to alleviate climate change would be a very effective solution that prevents future problems such as this arising.


## 1.1	Background Introduction

With over 1 billion metric tons grown annually, corn is the world’s most produced grain by volume, hundreds of millions of tons ahead of rice and wheat. In the 2018-2019 marketing year alone, approximately 2.5 trillion ears of corn (44.5 billion bushels) were consumed worldwide—the most food by volume of any crop. Such prevalence has earned corn the top ranking on Business Insider’s list of the most important crops in the world.

Corn is a great source of carbohydrates and dietary fiber, and contains a decent amount of protein, making it a nourishing food item. Additionally, corn is very nutritious, serving as a prime source of folate, thiamin, phosphorus, vitamin C, and magnesium, which explains its ability to sustain billions worldwide. 

Aside from its role as a ubiquitous and nutritional food, corn also can be converted into ethanol. Ethanol is an environmentally friendly, renewable fuel source that causes 43 percent less greenhouse gas emissions than gasoline. Use of ethanol thus far in the U.S. has had the equivalent carbon impact as removing 20 million cars from the road. Ethanol has even been named a “greenhouse gas-friendly alternative to fossil fuels” by U.S. Secretary of Agriculture Tom Vilsack. The ethanol fuel industry is also economically beneficial: in 2018 alone, it employed over 70,000 Americans and indirectly supported approximately 300,000 jobs nationwide. Consequently, corn-based ethanol has the potential to create a brighter, more sustainable future. 

Corn requires lots of natural resources to grow, more than any other U.S. crop: about 97 million acres of land in the U.S. are dedicated to corn production, and the crop uses about 5.6 cubic miles of irrigation water per year. Corn’s dual role as a source of nutrition and renewable energy make it a powerful and important crop. The United States is by far the largest producer, growing 755 billion ears of corn (15.1 billion bushels) annually and accounting for over one third of worldwide production. Within that, the top U.S. provider of corn is Iowa, boasting an impressive 135 billion ears of corn (2.7 billion bushels) produced annually from 12.2 million acres of dedicated farmland. Iowan corn comes from approximately 87,500 corn farms within the state, more than 97% of which are owned by farm families who depend on corn for their livelihood. In terms of ethanol, around 40% of all corn produced in Iowa is used to make ethanol, and around 30% of all U.S. ethanol comes from Iowan corn.

Strong statewide investment in a variety of sustainable farming practices by both the Iowa Department of Agriculture and Land Stewardship (IDALS) and various local communities has allowed Iowa to conserve soil and water over the years while continuing to expand their rate of production. One such practice is the planting of so-called “cover crops,” auxiliary non-commodity crops added to corn fields that provide soil maintenance to improve water quality, reduce erosion, combat weeds, and ultimately increase yields. 

Government backing provides the crucial force needed to research and promote the sustainable farming practices that make Iowa America’s top corn producer. For example, the IDALS provides financial subsidies to farmers who commit to planting cover crops and has established a number of government measures such as the Water Quality Initiative and Iowa Nutrient Reduction Strategy. They have also invested deeply in the construction and maintenance of agricultural infrastructure and waterways. Iowa’s local government and internal communities have made a commitment to sustainability and have ensured the state quality water access for the foreseeable future.

Iowa also owes its considerable corn production partly to a number of environmental factors. Iowa’s climate changes with the seasons with cold 15°F winters and warm 70°F summers. During the summer of 2019, Iowa’s average statewide temperature was 71.4°F with a standard deviation of aproximiatley 3.0°F between different countries. That summer, temperatures ranged as high 88.1°F as and as low as 54.7°F. Corn prospers in warm sunny weather, meaning Iowa’s long, hot summers provide the ideal environment for development during the growing season. Corn also requires moist, nitrogen-rich soil, but luckily Iowa’s fertile topsoil and humidity allows corn to thrive. Along with natural humidity, Iowa’s excellent government-backed irrigation systems allow farmers to supplement potential low humidity with extra water and safeguard against potential droughts.


# 2	Modeling


## 2.1	Data Methodology


### **2.1.a	Datasets**

As any living organism, corn crops can suffer detrimental effects when in a natural environment with a climate they are not accustomed to. Temperature is a particularly important climate factor in determining a corn crop’s ability to prosper, as too much heat will cause the plant to dry out, and too little will cause it to freeze over and die. Additionally, precipitation is important in order to prevent dehydration, but can also risk overwatering and root damage when unregulated.

Historic climate data in Iowa was needed both as a baseline from which to project future climate trends and as explanatory variables from which to build models for determining response variables. Datasets from the National Oceanic and Atmospheric Administration (NOAA) contained detailed historical data on maximum temperature (tMax), average temperature (tAvg), minimum temperature (tMin), and precipitation (pcpt).

The NOAA dataset was especially useful due to the number of useful datapoint characteristics provided with every climate value. Once the data was parsed, every datapoint in the dataset specifies the year, month, and county, it corresponds to, allowing for many different permutations of data organization and model structure which aids in the creation of a strong model.

An additional dataset was required in order to assess the impact of changes in climate factors on agriculture. Actuarial data from the United States Department of Agriculture (USDA) was able to be used to fill this role. The USDA provided two datasets: one containing detailed information on indemnified policies and one containing a broader overview of information on all crop insurance policies.

The dataset on indemnified policies was useful in providing specific insight into crop loss. Access to certain variables such as lost acres, planted acres, indemnified policies, and indemnity was especially useful because when combined with other variables as detailed in section 2.1.b, they were able to quantify important metrics such as severity of loss that became the foundations for predictive models. 

Furthermore, along with quantitative metrics, the indemnified USDA dataset also specified the cause of every loss recorded. This information allowed the dataset to be categorized that greatly aided in understanding the nature of crop loss. Using this information, three distinct categories were later defined to further the modeling process: a “Cold” category containing losses resulting from “cold wet weather”, “freeze”, and “frost”; a “Heat” category included containing losses resulting from “heat”; and an “Excess Moisture” category containing losses resulting from “excess moisture”.

One downside to the indemnified USDA dataset is that it contains relatively few data points for each county. With several thousand relevant data points in a given county, county-specific models failed to produce accurate results using our methodologies. However, the indemnified USDA dataset is luckily extremely expansive, allowing for the region of interest to be expanded all the way to the state-level, as was done for this paper, in order to produce an adequate number of data points to produce meaningful models.

The overview USDA dataset was especially helpful in contextualizing the indemnified USDA data. The metrics that described the number of indemnified policies and total number of policies insured annually allowed loss data to be understood as a part of the entire nationwide agricultural industry.


### **2.1.b	Derived Metrics**

Metrics were formulated to describe the frequency, probability, and severity of indemnities. 

Frequency was calculated as the total number of indemnified acres in a given year:



<p id="gdcalert1" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert2">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>



This value was then used to calculate Cost, found yearly by multiplying the expected lost acres and the average indemnity per acre:



<p id="gdcalert2" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert3">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>



Probability of loss for any given policy in a given month was found by calculating the proportion of all policies that were indemnified, as follows:



<p id="gdcalert3" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert4">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>



Where 

<p id="gdcalert4" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert5">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

 is the number of policies indemnified in the county that month, and _totalPolicies_ is the number of policies active that year.

Severity of loss for a given county in a given month was calculated as follows:



<p id="gdcalert5" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert6">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>



Where 

<p id="gdcalert6" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert7">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

 is the net acres possessed by all indemnified policies in the county that month, and 

<p id="gdcalert7" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert8">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

 is the net number of detrimented acres in those indemnified policies.


## 2.2	Mathematics Methodology

Parabolic regression models based on climate data from 1949-2019 were used to model the temperature and precipitation for 2020-2050. A feedforward neural network (FNN) was used to simulate the effect of climate change on corn production. The FNN was trained on historical climate data and resulting loss to corn crops. After the training process, the model was validated. The validated network was then used to predict future corn loss based off of our projected climate trends.


### **2.2.a	Explanatory Variables**

When modeling future weather patterns, it was important to make sure that both (a) enough past data was used in formulating the predictions and (b) the trendline fit the model well. 

The four climate variables from the NOAA dataset discussed in section 2.1.a (tMax, tAvg, tMin, and pcpt) were considered as independent variables. Data from the years 1949 to 2019 was used to create the model, as this provided a 70:30 split of 70 years of data to forecast the next 30 years.

Climate trends were found to be more apparent on a monthly level, rather than yearly or seasonal, as specification allowed for more accurate predictions. As such, projections were done on a monthly basis and utilized monthly data. The data points for each independent variable were segregated by month for separate regression modeling. 

Intrastate climate fluctuation between counties was then accounted for by averaging all of the month-specific county data to yield a dataset of Iowa-wide climate data discriminated by year.

To determine the optimal mathematical model, different types of regression models were tested. A polynomial regression was found to best model the historical data by maximizing the squares of the Pearson product-moment correlation coefficients (R<sup>2</sup>), in order to most accurately predict the weather values. 

These dataset were then plotted against year time series, and fit to a 2nd degree polynomial regression, yielding 48 regression equations—12 for each independent variable.

These regressions were used to project future climate trends through to 2050. The predicted values were then used to calculate frequency, probability, and severity.



<p id="gdcalert8" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Paper0.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert9">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Paper0.png "image_tooltip")




<p id="gdcalert9" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Paper1.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert10">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Paper1.png "image_tooltip")




<p id="gdcalert10" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Paper2.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert11">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Paper2.png "image_tooltip")




<p id="gdcalert11" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Paper3.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert12">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Paper3.png "image_tooltip")


_See Appendix A for regression equations._


### **2.2.b	Frequency**

Frequency, as calculated by the number of indemnified policies in a year, was calculated separately for losses resulting from Cold, Heat, and Excess Moisture. Future frequencies through 2050 were predicted with a least-squares regression line that used the frequencies from 1991-2019 as data points. To calculate cost, indemnities per acre was calculated and projected the same way that frequency was, except using (_average indemnityAmount)/year_ as the x-values for the least-squares regression.


<table>
  <tr>
   <td colspan="2" ><em>Table 2.3.v.1 Temperature Predictions</em>
   </td>
  </tr>
  <tr>
   <td><strong>Cause of Loss</strong>
   </td>
   <td><p style="text-align: right">
<strong>Equation for Yearly Lost Acres, x = Year</strong></p>

   </td>
  </tr>
  <tr>
   <td><strong>Cold</strong>
   </td>
   <td><p style="text-align: right">
<code>-215x + 464884</code></p>

   </td>
  </tr>
  <tr>
   <td><strong>Heat</strong>
   </td>
   <td><p style="text-align: right">
<code>547x - 1080000</code></p>

   </td>
  </tr>
  <tr>
   <td><strong>Excess Moisture</strong>
   </td>
   <td><p style="text-align: right">
<code>13889x - 27200000</code></p>

   </td>
  </tr>
</table>



### **2.2.c	Probability**

Probability of loss, calculated as the number of indemnified policies over total policies, was also calculated separately for losses resulting from Cold, Heat, and Excess Moisture. For each of these, the data was aggregated by average, and a trendline that best fit the data was added. The created model would allow for the interpolation of data given a temperature, so the predicted weather value would be plugged in to the probability equation to find the probability of any given policy being indemnified due to Cold, Heat, or Excess Moisture. 

The probability for loss from Cold, as well as loss from Heat, was calculated using tAvg on the x-axis, as for each of those, that was the variable that showed an association while the others did not. The probability for loss from Excess Moisture was calculated using precipitation values for the x-axis. This makes sense, as excess moisture is likely a result of too much water which is forced onto the plants via precipitation, rather than a temperature variable. The best fit to provide the most accurate interpolation values for losses from Cold appeared to be a mapping to an 8th degree polynomial, while the remaining 2 followed exponential models.



<p id="gdcalert12" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Paper4.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert13">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Paper4.png "image_tooltip")




<p id="gdcalert13" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Paper5.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert14">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Paper5.png "image_tooltip")


<p id="gdcalert14" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Paper6.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert15">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Paper6.png "image_tooltip")



### **2.2.d	Severity**

When modeling complexly intertwined relationships in the real world, standard modeling can often overlook subtle and hard to detect trends. With modern-day advancements in machine learning, neural networks are often able to produce more accurate models than their traditional counterparts in these cases.

A Feedforward Neural Network (FNN) is a powerful type of Neural Network that can learn to model interconnected relations between a set of input variables and output variables from a set of training data. A FNN was configured to take independent variables (tMax, tAvg, tMin, pcpt) as input values and output a severity percentage to model the impact of climate factors on crop loss.

Historic independent variable data from section 2.1.a and severity values from section 2.1.b were compiled into a training dataset that specified the tMax, tAvg, tMin, pcpt, and corresponding severity in every county in Iowa for every month with a recorded loss, yielding a dataset of 17,673 historic relations between climate factors.

Temperature data and precipitation data were then normalized between 0 and 1 for optimal FNN training.

Then data was divided into a set of training data and validation data using a 70-30 split. Importance was placed on dividing the data with an split that had an even distribution of years, counties, and months to reduce bias in model training. In order to ensure that data has this even distribution a pseudo-random algorithm to divide the data was developed.

The algorithm assigned every country an integer identification number between 0 and 98 represented months as numbers on a 0 to 11 scale. These two numbers, along with the year number, were used to characterize each datapoint, allowing for the creation of the following criterion expression:



<p id="gdcalert15" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert16">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>



This expression was evaluated for every datapoint 17,673-point dataset, with data points which met the criterion being placed in the validation dataset and the remaining data points used as training data.

These normalized, organized, fully-processed datasets were then ready to be fed into a FNN.

The FNN itself was created in Python 3 using the `keras` library, a high-level programming interface designed for the creation of neural networks.[^1]

A FNN with three hidden layers of nodes was created. 



<p id="gdcalert16" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Paper7.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert17">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Paper7.png "image_tooltip")


_Fig. 2.2.d.1 Visualization of the Neural Network’s Architecture_[^2]

Neural networks operate through sequences of interconnected “nodes” grouped into “layers” intended to mimic the neurons of an organic brain. Each of these nodes represents a number, or “activation” determined by the outcome of some function.

The FNN created to model climate impact on severity used the activation function:



<p id="gdcalert17" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert18">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>



Where 

<p id="gdcalert18" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert19">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

 is an input from another node and

<p id="gdcalert19" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert20">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

 and 

<p id="gdcalert20" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert21">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

 are the specific node’s “weight” and “bias” respectively. 

In the first layer our neural networks takes this 

<p id="gdcalert21" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert22">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

 input from the four independent variables, and subsequent layers use the activation of preceding layer nodes as their 

<p id="gdcalert22" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert23">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

 input. This process continues until the neural network reaches its final layer, where the result of the output function is taken as the predicted dependent variable value.

As such, the output of the neural network is entirely dependent on the values of each node’s 

<p id="gdcalert23" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert24">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

 and 

<p id="gdcalert24" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert25">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

. Hence, the process of “training” a neural network is the automated process of fine tuning hundreds of these interconnected weights and biases to minimize the “cost” of the network, the difference between the neural network’s final output layer and the training data

That cost was quantified as the Mean Squared Error (MSE):



<p id="gdcalert25" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert26">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>



Where 

<p id="gdcalert26" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert27">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

 is the number of datapoints being used to train the network, which in this case is 17,673. 

<p id="gdcalert27" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert28">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

 denotes the severity predicted by the neural network for datapoint 

<p id="gdcalert28" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert29">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

 and 

<p id="gdcalert29" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert30">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

 denotes the corresponding historical severity for that datapoint.

A quantitative assessment of the FNN’s performance allows for iterative improvement. By extensive use of the chain rule, the partial derivatives of cost with respect to any given weight or bias can be calculated. Then every weight and bias is decreased by its partial derivative to decrease the cost of the FNN, thus completing the mathematical solution for fine tuning the network’s weights and biases by minimizing cost.



<p id="gdcalert30" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert31">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>





<p id="gdcalert31" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert32">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>



Where 

<p id="gdcalert32" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert33">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

 and 

<p id="gdcalert33" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert34">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

 denote the weight and bias of node 

<p id="gdcalert34" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert35">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

.

This fine tuning of weights and biases was then iteratively repeated 2500 times, to progressively nudge the FNN towards a more accurate model.

Just as the MSE cost was used as a quantitative assessment of the FNN to train the network, MSE can be used in conjunction with the validation dataset to assess the correlation of the trained FNN’s model, similarly to how one might measure the R<sup>2</sup> of regression equations.



<p id="gdcalert35" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Paper8.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert36">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Paper8.png "image_tooltip")


_Fig. 2.2.d.2 Feedforward Neural Network Learning Progression_

By the end of training at iteration 2500, the FNN had a low cost of 3.22%, proving itself to be a strong predictive model.[^3]


## 2.3	Results


### **2.3.a	Independent Variables**

Our models project that Iowa will experience an upward parabolic trend in temperature over the next 30 years. This makes sense, because Iowa is not near the equator or the arctic circle, areas more affected by climate change than others. Precipitation has a strong, linear, upward trend and average precipitation per month is expected to continue increasing. 


<table>
  <tr>
   <td colspan="5" ><em>Table 2.3.a.1 Temperature Predictions</em>
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td><strong>tMax</strong>
   </td>
   <td><strong>tAvg</strong>
   </td>
   <td><strong>tMin</strong>
   </td>
   <td><strong>pcpt</strong>
   </td>
  </tr>
  <tr>
   <td><strong>2020</strong>
   </td>
   <td><p style="text-align: right">
<code>58.97560</code></p>

   </td>
   <td><p style="text-align: right">
<code>48.79748</code></p>

   </td>
   <td><p style="text-align: right">
<code>38.61533</code></p>

   </td>
   <td><p style="text-align: right">
<code>3.15213</code></p>

   </td>
  </tr>
  <tr>
   <td><strong>2050</strong>
   </td>
   <td><p style="text-align: right">
<code>60.26157</code></p>

   </td>
   <td><p style="text-align: right">
<code>50.11724</code></p>

   </td>
   <td><p style="text-align: right">
<code>39.96977</code></p>

   </td>
   <td><p style="text-align: right">
<code>3.58985</code></p>

   </td>
  </tr>
  <tr>
   <td><strong>Change factor</strong>
   </td>
   <td><p style="text-align: right">
<code>2.181%</code></p>

   </td>
   <td><p style="text-align: right">
<code>2.705%</code></p>

   </td>
   <td><p style="text-align: right">
<code>3.508%</code></p>

   </td>
   <td><p style="text-align: right">
<code>13.89%</code></p>

   </td>
  </tr>
</table>



### **2.3.b	Frequency**

As seen from the frequency models in 2.2b, frequency is expected to increase for losses from Heat and losses from Excess Moisture. On the other hand, losses from Cold are expected to decrease, very slightly, which makes sense because of the global warming phenomenon that temperatures are rising so there will be less losses from Cold.

This model predicts that by 2050, the frequency of loss will increase to 1,337,934 indemnified acres per year, a 426,630 acre increase from present day values.

To calculate the total expected cost, the categorized yearly frequencies _(lostAcres/year)_ were multiplied by the_ average yearly indemnity/Acre _(found in 2.2b). The total expected cost had a very strong, positive linear association, and is expected to increase steadily in the future (graph shown in Risk Analysis section). The total cost is expected to almost triple between 2020 and 2050, reaching an expected value of $285,415,475.59 in 2050.


### **2.3.c	Probability**

For predicting probability, the equations in the probability models were used to predict the probabilities of any selected policy in a given year and month for the 3 cause of loss categories in the future years based on the predicted temperature. These were then summed to calculate the total probability: the y-value, being the probability that any selected policy would be indemnified from cold, heat, or excess moisture. The expected probability followed an almost perfect positive linear trend.



<p id="gdcalert36" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Paper9.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert37">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Paper9.png "image_tooltip")



### **2.3.d	Severity**

The trained FNN model used to predict the future severity of corn losses given the climate factor predictions from section 2.2.a as input, yielding a list of monthly severity predictions from 2020 to 2050. Of this data, the sample from May to September was extracted for further analysis, as that tends to be the time during which corn is grown in Iowa.

The data was then aggregated to find a series of yearly average loss severities 



<p id="gdcalert37" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Paper10.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert38">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Paper10.png "image_tooltip")


As modeled by the FNN, severity of loss increases from 90.346 percentage-points in 2020 to 92.349 percentage-points in 2050, or a 2.003 percentage-point increase over 30 years.


# 3	Analysis


## 3.1	Risk Analysis

While the corn industry in only one state may not seem so important, the risks to the Iowa corn industry present risks to the many other industries supported by Iowan corn. It is also necessary to consider that much of the Iowan conclusions can be applied to similar states across the nation—particularly other states in the Corn Belt which tend to share similar climates and are also top national producers of corn, for instance Illinois, Nebraska, and Minnesota.

When analyzing the risks for Iowan corn, the probability of any given policy being indemnified due to weather variables is gradually increasing as temperatures rise. Heat stress experienced in high temperatures causes damage to corn crops and can be detrimental to yield. Looking at the expected cost trendline below, we can see that the expected total indemnity increases rapidly and is approaching $300 million (almost tripling from 2020) by the year 2050, which is alarming. 



<p id="gdcalert38" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/Paper11.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert39">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/Paper11.png "image_tooltip")


The severity of the indemnities was also seen to be steadily increasing. Indeed, climate change is expected to intensify heavy rain events, which had the most significant effect on corn loss, especially as was seen in the Midwest in the spring of 2019, when flooding caused billions of dollars in crop and infrastructure damage. In states like Iowa, an emphasis on controlled water exposure in the form of protection from aggressive and overwhelming rainfall outweighs the need to improve already high-functioning irrigation systems.

However, excessive rainfall is a serious problem. Abrasive runoff can erode soil and sweep away crucial phosphorus, which can result in reduced yield or even potentially physically sweep away crops or lead to nutrient-deprivation induced death. Rainfall poses a recurring long-term problem because gradual erosion of a limited amount of soil and its limited nutrients will eventually degrade Iowa’s fertile land and inhibit corn growth and production. With projections only predicting increases in rainfall in the future, Iowa corn crops are at serious risk of the deadly threats of soil erosion and nutrient deprivation.

All of these factors combined will likely be a burden for small farmers to bear, and might deter business in the Iowa corn industry. Remembering that 97% of Iowa corn farms are family farms, the results of the changes in weather patterns have the possibility of having a severe impact on those farmers’ livelihoods and/or pushing people into poverty.

In addition, as corn is integral in the ethanol and livestock industries, there will likely be a spillover effect on them. 

The ethanol industry will likely be significantly impacted, as 30% of all U.S. ethanol comes from Iowan corn alone. Ethanol, a biofuel, plays a big role in keeping the environment cleaner than other forms of fuel, such as fossil fuels. Harms to the corn industry can lead to a slight shift away from ethanol production and use, towards unclean forms of fuel. This is dangerous because it will only perpetuate the cycle of climate change that is harming the corn industry in the first place. For instance, E85 is a type of fuel that is generally 85% ethanol and 15% gasoline. The combustion of E85 produces 39% less carbon dioxide than the combustion of  regular gasoline, and ethanol itself is carbon neutral because the amount of carbon dioxide produced by burning the ethanol is equal to the amount of carbon dioxide absorbed by the corn plant during its lifetime. 

 Corn for livestock feed is also a byproduct within the ethanol industry, and about one in every three bushels of corn processed by an ethanol biorefinery are used in livestock feed. Corn accounts for upwards of 95 percent of feed grain for livestock, indicating that the livestock industry would also experience a shock if the corn industry does. The livestock industry is incredibly important to the U.S. economy: it generates property taxes and increases incomes, as the livestock industry supports upwards of 1.8 million jobs in rural America, contributes upwards of $250 billion to GDP each year, and has contributed more than $41 billion to U.S. household incomes. The impacts on this industry would likely lead to layoffs and increase the prices of animal products nationwide.

Overall, accounting for workers in the corn industry, livestock industry, ethanol industry, and all industries relating to those, millions of people have jobs that rely on or are interconnected with the Iowa corn industry, and thus any risk to the corn industry is a risk of large scope and varied impact.


## 3.2	Recommendations

Insurance companies will likely experience the most direct impact from the changing climate, to which the most reasonable logical follow-up would be raising premiums to account for the increased expected cost, frequency, severity, and probability of indemnities. Or, as the severity of indemnities is increasing, it might be in the best interest of the insurance companies to change their policies so that they are liable for a smaller percentage of acres.

In order to keep small family farms in business, it is recommended that the government increases the subsidies for small family farms who specialize in corn in Iowa. As corn and its many uses affect a wide range of industries, government subsidies for farmers would help combat the projected increases in losses and keep farmers in business. It would also encourage pursuing an agricultural career and investing in corn, as subsidies and insurance are what makes such a risky industry possible to do business in. Although, while this is likely the best course of action as it will help stabilize the economy, it is worth mentioning that the money for the subsidies is being taken out of the federal budget and could have been used for something else (or, it will come as a result of raising taxes, which would have much more far-reaching consequences in terms of behavior of the electorate).

Another suggestion for the government is increasing investment in the ethanol industry, as expanding the ethanol industry will create a higher demand for corn, helping ensure that corn stays profitable to farm, thereby encouraging small farmers to stay in the business. One way to do this would be to invest in more E85 filling stations and the conversion of regular gasoline stations into E85 filling stations, of which there are currently approximately only 4,800 (out of over 100,000 total gas stations in the U.S.). In addition, increasing the amount of Flex Fuel Vehicles, vehicles that can safely run on blends of ethanol and oil, in circulation would also increase ethanol demand. Unfortunately, from 2015 to 2020 there has been a decline in the number of Flex Fuel Vehicle models being manufactured by major brands such as Ford and General Motors, despite a rising demand for them. Addressing this, the U.S. government could pass a policy to instate a quota on Flex Fuel Vehicle production for major auto companies and subsidize the production of Flex Fuel Vehicles compatible with E85 to accelerate the shift from gasoline to ethanol. Not only would these governmental actions help corn farmers, following from the environmental benefits of E85 discussed earlier, there would also be an environmental benefit as there would be fewer vehicular emissions to contribute to global warming. 

The United States federal government taking steps to mitigate climate change, especially as a world leader, is likely the most effective long term solution. In addition to the actions mentioned in the above paragraph, this could be achieved more broadly by increasing investment in green technology, such as wind and solar power, and making green tech economical, increasing investment in carbon sequestration and managing the nitrogen cycle, placing and enforcing stricter regulations on emissions for manufacturers, and protecting and restoring key ecosystems, which play an integral role in fighting global warming. 

For farmers, we recommend stocking up on extra mulch and perlite. When placed around crop roots, they can help regulate moisture to protect against excessive rainfall. But in the long-term, more drastic measures will need to be taken. In preparation to deal with abrasive rainfall, new planting techniques must be employed to protect against destructive soil erosion and nutrient depletion. We propose three strategies: no-till farming, terraces, and stream buffers.

First is a maintenance practice called “no-till farming,” a highly economical and efficient technique whereby farmers simply leave soil and crop residue undisturbed between harvest and planting rather than overturning it with tilling equipment. Soil can be injected with nutrients if necessary. This tactic significantly reduces soil disturbance, promotes accelerated root growth, and allows for prolonged buildup of organic matter in soil. The end result of this is reduced soil erosion and heightened natural nutrient generation from within the soil.

Second is building terraces, a planting technique where crops are vertically staggered on slopes of soil, allowing the gradual descent to slow water runoff. Doing so both slows erosion by preventing soil from being carried away by rapid runoff and helps maintain critical nutrients in soil. Additionally, terraces prevent water loss by trapping rainwater in non-destructive form, allowing for crops to gradually absorb it.

Third is developing stream buffers, the more complicated of the three techniques, but potentially the one with the greatest payoff both in terms of yield and long term environmental sustainability. Somewhat similarly to cover-crops, stream buffers are essentially just plant life placed around nearby runoff streams and waterways. The plants trap various sediments broken off by abrasive runoff, allowing crops to reabsorb nutrients that otherwise would have been lost and making sure to preserve soil matter. Additionally, the trapping of excess sediment stabilizes the waterways themselves, improving stream flow and protecting the habitats of local wildlife. 

	Overall, we believe that if the above recommendations are considered, they will significantly offset the adverse effects of climate change on Iowan corn. 

	


# Appendix A


<table>
  <tr>
   <td colspan="5" ><strong>Equations for Independent Variable Projection</strong>
   </td>
  </tr>
  <tr>
   <td><strong>Month</strong>
   </td>
   <td><strong>Variable</strong>
   </td>
   <td><strong>Equation</strong>
   </td>
   <td><strong>Variable</strong>
   </td>
   <td><strong>Equation</strong>
   </td>
  </tr>
  <tr>
   <td>January
   </td>
   <td rowspan="12" >tMin
   </td>
   <td>9.76E-4x² - 3.79E+0x + 3.68E+3
   </td>
   <td rowspan="12" >tAvg
   </td>
   <td>9.59E-4x² - 3.74E+0x + 3.66E+3
   </td>
  </tr>
  <tr>
   <td>February
   </td>
   <td>-9.08E-4x² + 3.63E+0x - 3.62E+3
   </td>
   <td>-8.16E-4x² + 3.25E+0x - 3.21E+3
   </td>
  </tr>
  <tr>
   <td>March
   </td>
   <td>-1.69E-3x² + 6.79E+0x - 6.79E+3
   </td>
   <td>-2.04E-3x² + 8.19E+0x - 8.17E+3
   </td>
  </tr>
  <tr>
   <td>April
   </td>
   <td>-1.46E-3x² + 5.81E+0x - 5.75E+3
   </td>
   <td>-1.29E-3x² + 5.14E+0x - 5.07E+3
   </td>
  </tr>
  <tr>
   <td>May
   </td>
   <td>3.17E-4x² - 1.24E+0x + 1.27E+3
   </td>
   <td>1.78E-4x² - 7.06E-1x + 7.58E+2
   </td>
  </tr>
  <tr>
   <td>June
   </td>
   <td>1.16E-3x² - 4.58E+0x + 4.58E+3
   </td>
   <td>7.58E-4x² - 2.99E+0x + 3.03E+3
   </td>
  </tr>
  <tr>
   <td>July
   </td>
   <td>-1.80E-4x² + 7.37E-1x - 6.90E+2
   </td>
   <td>-1.55E-4x² + 6.19E-1x - 5.44E+2
   </td>
  </tr>
  <tr>
   <td>August
   </td>
   <td>-3.19E-4x² + 1.28E+0x - 1.23E+3
   </td>
   <td>-2.59E-4x² + 1.03E+0x - 9.49E+2
   </td>
  </tr>
  <tr>
   <td>September
   </td>
   <td>7.35E-4x² - 2.86E+0x + 2.83E+3
   </td>
   <td>1.18E-3x² - 4.62E+0x + 4.60E+3
   </td>
  </tr>
  <tr>
   <td>October
   </td>
   <td>1.05E-3x² - 4.15E+0x + 4.16E+3
   </td>
   <td>1.31E-3x² - 5.23E+0x + 5.26E+3
   </td>
  </tr>
  <tr>
   <td>November
   </td>
   <td>-1.02E-3x² + 4.10E+0x - 4.08E+3
   </td>
   <td>1.69E-4x² - 6.42E-1x + 6.44E+2
   </td>
  </tr>
  <tr>
   <td>December
   </td>
   <td>1.91E-3x² - 7.53E+0x + 7.43E+3
   </td>
   <td>2.03E-3x² - 8.01E+0x + 7.93E+3
   </td>
  </tr>
  <tr>
   <td>January
   </td>
   <td rowspan="12" >tMax
   </td>
   <td>9.38E-4x² - 3.67E+0x + 3.62E+3
   </td>
   <td rowspan="12" >pcpt
   </td>
   <td>1.43E-4x² - 5.70E-1x + 5.68E+2
   </td>
  </tr>
  <tr>
   <td>February
   </td>
   <td>-7.22E-4x² + 2.86E+0x - 2.80E+3
   </td>
   <td>4.88E-4x² - 1.93E+0x + 1.92E+3
   </td>
  </tr>
  <tr>
   <td>March
   </td>
   <td>-2.39E-3x² + 9.58E+0x - 9.55E+3
   </td>
   <td>-9.38E-5x² + 3.68E-1x - 3.59E+2
   </td>
  </tr>
  <tr>
   <td>April
   </td>
   <td>-1.12E-3x² + 4.46E+0x - 4.39E+3
   </td>
   <td>-7.32E-5x² + 3.04E-1x - 3.11E+2
   </td>
  </tr>
  <tr>
   <td>May
   </td>
   <td>3.78E-5x² - 1.62E-1x + 2.44E+2
   </td>
   <td>4.55E-4x² - 1.78E+0x + 1.75E+3
   </td>
  </tr>
  <tr>
   <td>June
   </td>
   <td>3.50E-4x² - 1.39E+0x + 1.46E+3
   </td>
   <td>8.67E-4x² - 3.42E+0x + 3.39E+3
   </td>
  </tr>
  <tr>
   <td>July
   </td>
   <td>-1.28E-4x² + 4.94E-1x - 3.90E+2
   </td>
   <td>-4.60E-4x² + 1.83E+0x - 1.81E+3
   </td>
  </tr>
  <tr>
   <td>August
   </td>
   <td>-1.97E-4x² + 7.62E-1x - 6.55E+2
   </td>
   <td>5.50E-5x² - 2.08E-1x + 1.99E+2
   </td>
  </tr>
  <tr>
   <td>September
   </td>
   <td>1.62E-3x² - 6.39E+0x + 6.38E+3
   </td>
   <td>-1.52E-4x² + 6.13E-1x - 6.14E+2
   </td>
  </tr>
  <tr>
   <td>October
   </td>
   <td>1.58E-3x² - 6.30E+0x + 6.35E+3
   </td>
   <td>7.70E-5x² - 2.90E-1x + 2.74E+2
   </td>
  </tr>
  <tr>
   <td>November
   </td>
   <td>1.36E-3x² - 5.38E+0x + 5.36E+3
   </td>
   <td>-7.27E-4x² + 2.89E+0x - 2.87E+3
   </td>
  </tr>
  <tr>
   <td>December
   </td>
   <td>2.15E-3x² - 8.50E+0x + 8.43E+3
   </td>
   <td>1.10E-4x² - 4.29E-1x + 4.17E+2
   </td>
  </tr>
</table>




Bibliography


    “2020 Vehicle Models Bring Good News for E15, Bad News for Flex Fuels.” Convenience Store News_. _December 12, 2019. https://csnews.com/2020-vehicle-models-bring-good-news-e15-bad-news-flex-fuels


    Agri-Pulse Staff. “Animal Agriculture Created over 1.8 Million Jobs in Rural America.” AgriPulse Communications, March 9, 2011. https://www.agri-pulse.com/articles/1010-animal-agriculture-created-over-1-8-million-jobs-in-rural-america.


    Arnarson, Atli. “Corn 101: Nutritional Facts and Health Benefits.” May 16, 2019. https://www.healthline.com/nutrition/foods/corn


    “Corn Uses.” Iowa Corn. Accessed February 29, 2020. https://www.iowacorn.org/corn-uses.


    Delp, Rachel. “Ideal Climate & Soil for Corn Growth.” SFGate_, _December 15, 2018. https://homeguides.sfgate.com/ideal-climate-soil-corn-growth-37426.html


    “Feed Grains Sector at a Glance.” USDA ERS - Feed Grains Sector at a Glance. Accessed February 29, 2020. https://www.ers.usda.gov/topics/crops/corn-and-other-feedgrains/feedgrains-sector-at-a-glance/.


    “Food & Ag Industry Contributes $992 Billion to U.S. Economy.” AG Web, April 7, 2017. https://www.agweb.com/article/food--ag-industry-contributes-992-billion-to-us-economy-NAA-ben-potter.


    Gabrick, Andrea. “Summer Corn -- More than Delicious.” WebMD_, _July 02, 2009. https://www.webmd.com/diet/features/summer-corn-more-than-delicious


    Hardesty, Larry. “Explained: Neural Networks.” MIT News, April 14, 2017. http://news.mit.edu/2017/explained-neural-networks-deep-learning-0414.


    “Iowa's Corn and Agriculture Industry.” Iowa Culture. Accessed February 29, 2020. https://iowaculture.gov/history/education/educator-resources/primary-source-sets/iowas-corn-and-agriculture-industry.


    Kassel, Kathleen. “Farming and Farm Income.” USDA ERS - Farming and Farm Income, February 5, 2020. https://www.ers.usda.gov/data-products/ag-and-food-statistics-charting-the-essentials/farming-and-farm-income/.


    Licht, Mark. “Late Corn Planting Options.” Iowa State University, May 9, 2019. https://crops.extension.iastate.edu/cropnews/2019/05/late-corn-planting-options.


    “Majority of Crop Acres Covered by Crop Insurance.” American Farm Bureau Federation. April 29, 2019. https://www.fb.org/market-intel/majority-of-crop-acres-covered-by-crop-insurance.


    Maslowski, Debra. “Soil Moisture: How to Deal with Excess and Lack.” DIY Natural_. _https://www.diynatural.com/soil-moisture/


    “Neural Networks - What Are They and Why Do They Matter?” SAS. Accessed February 29, 2020. https://www.sas.com/en_us/insights/analytics/neural-networks.html.


    “Stream Buffers.” New York State Department of Environmental Conservation. [http://www.dec.ny.gov/docs/remediation_hudson_pdf/hrewfssb1.pdf](http://www.dec.ny.gov/docs/remediation_hudson_pdf/hrewfssb1.pdf?fbclid=IwAR2mfXbcWAHQG9ZjAU8g0bY-zZU5tqi-IRvbGnf2BJ5a15TH371NaZEGNfs)


    “Temperature, Precipitation, and Drought.” National Oceanic and Atmospheric Association (NOAA), 2020. [https://www.ncdc.noaa.gov/temp-and-precip/](https://www.ncdc.noaa.gov/temp-and-precip/)


    “POURING IT ON: How Climate Change Intensifies Heavy Rain Events.” Climate Central, May 15, 2019. https://www.climatecentral.org/news/report-pouring-it-on-climate-change-intensifies-heavy-rain-events.


    The Editors of Encyclopaedia Britannica. “Corn Belt.” Encyclopædia Britannica. Encyclopædia Britannica, inc., September 26, 2016. https://www.britannica.com/place/Corn-Belt.


    The Editors of Encyclopaedia Britannica. “Corn.” Encyclopædia Britannica. Encyclopædia Britannica, inc., February 13, 2020. https://www.britannica.com/plant/corn-plant.


    United States Department of Agriculture (USDA RMA), 2019, _Cause of Loss Historical Data Files_, accessed February 2019. [https://www.rma.usda.gov/Information-Tools/Summary-of-Business/Cause-of-Loss](https://www.rma.usda.gov/Information-Tools/Summary-of-Business/Cause-of-Loss?fbclid=IwAR3O13QGQ80GpMJtHmbQG7vZZVrYyWng0EbEc4gNOlJhKdR1nFZiJ1hhJ7U).


    “Why Is Ethanol Important?” Renewable Fuels Association. Accessed February 29, 2020. https://ethanolrfa.org/consumers/why-is-ethanol-important/.


    “World of Corn 2019.”_ _National Corn Growers Association. 2019. http://www.worldofcorn.com/pdf/WOC-2019.pdf


    Yaniz, Laura. “5 ways our government can confront climate change.” AIDA. November 17, 2017. [https://aida-americas.org/en/blog/5-ways-our-governments-can-confront-climate-change](https://aida-americas.org/en/blog/5-ways-our-governments-can-confront-climate-change)


    Zwass, Vladimir. “Neural Network.” Encyclopædia Britannica. Encyclopædia Britannica, inc., January 9, 2020. https://www.britannica.com/technology/neural-network.


<!-- Footnotes themselves at the bottom. -->
## Notes

[^1]:
     See [https://keras.io/](https://keras.io/) for documentation on the keras library.

[^2]:
     Web application [http://alexlenail.me/NN-SVG/AlexNet.html](http://alexlenail.me/NN-SVG/AlexNet.html) used for image generation

[^3]:
     All of the code used to create this neural network, along with all data parsing involved in this project and much of the statistical analysis is publicly available at [https://github.com/bickerforrest/TeamRocketMTF](https://github.com/bickerforrest/TeamRocketMTF)


<!-- Docs to Markdown version 1.0β22 -->
