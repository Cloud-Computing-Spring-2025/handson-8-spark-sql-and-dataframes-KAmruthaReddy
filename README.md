# handson-08-sparkSQL-dataframes-social-media-sentiment-analysis

## **Prerequisites**

Before starting the assignment, ensure you have the following software installed and properly configured on your machine:

1. **Python 3.x**:
   - [Download and Install Python](https://www.python.org/downloads/)
   - Verify installation:
     ```bash
     python3 --version
     ```

2. **PySpark**:
   - Install using `pip`:
     ```bash
     pip install pyspark
     ```

3. **Apache Spark**:
   - Ensure Spark is installed. You can download it from the [Apache Spark Downloads](https://spark.apache.org/downloads.html) page.
   - Verify installation by running:
     ```bash
     spark-submit --version
     ```

4. **Docker & Docker Compose** (Optional):
   - If you prefer using Docker for setting up Spark, ensure Docker and Docker Compose are installed.
   - [Docker Installation Guide](https://docs.docker.com/get-docker/)
   - [Docker Compose Installation Guide](https://docs.docker.com/compose/install/)

## **Setup Instructions**

### **1. Project Structure**

Ensure your project directory follows the structure below:

```
SocialMediaSentimentAnalysis/
├── input/
│   ├── posts.csv
│   └── users.csv
├── outputs/
│   ├── hashtag_trends.csv
│   ├── engagement_by_age.csv
│   ├── sentiment_engagement.csv
│   └── top_verified_users.csv
├── src/
│   ├── task1_hashtag_trends.py
│   ├── task2_engagement_by_age.py
│   ├── task3_sentiment_vs_engagement.py
│   └── task4_top_verified_users.py
├── docker-compose.yml
└── README.md
```



- **input/**: Contains the input datasets (`posts.csv` and `users.csv`)  
- **outputs/**: Directory where the results of each task will be saved.
- **src/**: Contains the individual Python scripts for each task.
- **docker-compose.yml**: Docker Compose configuration file to set up Spark.
- **README.md**: Assignment instructions and guidelines.

### **2. Running the Analysis Tasks**

You can run the analysis tasks either locally or using Docker.

#### **a. Running Locally**

1. **Navigate to the Project Directory**:
   ```bash
   cd SocialMediaSentimentAnalysis/
   ```

2. **Execute Each Task Using `spark-submit`**:
   ```bash
 
     spark-submit src/task1_hashtag_trends.py
     spark-submit src/task2_engagement_by_age.py
     spark-submit src/task3_sentiment_vs_engagement.py
     spark-submit src/task4_top_verified_users.py
     
   ```

3. **Verify the Outputs**:
   Check the `outputs/` directory for the resulting files:
   ```bash
   ls outputs/
   ```

#### **b. Running with Docker (Optional)**

1. **Start the Spark Cluster**:
   ```bash
   docker-compose up -d
   ```

2. **Access the Spark Master Container**:
   ```bash
   docker exec -it spark-master bash
   ```

3. **Navigate to the Spark Directory**:
   ```bash
   cd /opt/bitnami/spark/
   ```

4. **Run Your PySpark Scripts Using `spark-submit`**:
   ```bash
   
   spark-submit src/task1_hashtag_trends.py
   spark-submit src/task2_engagement_by_age.py
   spark-submit src/task3_sentiment_vs_engagement.py
   spark-submit src/task4_top_verified_users.py
   ```

5. **Exit the Container**:
   ```bash
   exit
   ```

6. **Verify the Outputs**:
   On your host machine, check the `outputs/` directory for the resulting files.

7. **Stop the Spark Cluster**:
   ```bash
   docker-compose down
   ```

## **Overview**

In this assignment, you will leverage Spark Structured APIs to analyze a dataset containing employee information from various departments within an organization. Your goal is to extract meaningful insights related to employee satisfaction, engagement, concerns, and job titles. This exercise is designed to enhance your data manipulation and analytical skills using Spark's powerful APIs.

## **Objectives**

By the end of this assignment, you should be able to:

1. **Data Loading and Preparation**: Import and preprocess data using Spark Structured APIs.
2. **Data Analysis**: Perform complex queries and transformations to address specific business questions.
3. **Insight Generation**: Derive actionable insights from the analyzed data.

## **Dataset**

## **Dataset: posts.csv **

You will work with a dataset containing information about **100+ users** who rated movies across various streaming platforms. The dataset includes the following columns:

| Column Name     | Type    | Description                                           |
|-----------------|---------|-------------------------------------------------------|
| PostID          | Integer | Unique ID for the post                                |
| UserID          | Integer | ID of the user who posted                             |
| Content         | String  | Text content of the post                              |
| Timestamp       | String  | Date and time the post was made                       |
| Likes           | Integer | Number of likes on the post                           |
| Retweets        | Integer | Number of shares/retweets                             |
| Hashtags        | String  | Comma-separated hashtags used in the post             |
| SentimentScore  | Float   | Sentiment score (-1 to 1, where -1 is most negative)  |


---

## **Dataset: users.csv **
| Column Name | Type    | Description                          |
|-------------|---------|--------------------------------------|
| UserID      | Integer | Unique user ID                       |
| Username    | String  | User's handle                        |
| AgeGroup    | String  | Age category (Teen, Adult, Senior)   |
| Country     | String  | Country of residence                 |
| Verified    | Boolean | Whether the account is verified      |

---

### **Sample Data**

Below is a snippet of the `posts.csv`,`users.csv` to illustrate the data structure. Ensure your dataset contains at least 100 records for meaningful analysis.

```
PostID,UserID,Content,Timestamp,Likes,Retweets,Hashtags,SentimentScore
101,1,"Loving the new update! #tech #innovation","2023-10-05 14:20:00",120,45,"#tech,#innovation",0.8
102,2,"This app keeps crashing. Frustrating! #fail","2023-10-05 15:00:00",5,1,"#fail",-0.7
103,3,"Just another day... #mood","2023-10-05 16:30:00",15,3,"#mood",0.0
104,4,"Absolutely love the UX! #design #cleanUI","2023-10-06 09:10:00",75,20,"#design,#cleanUI",0.6
105,5,"Worst experience ever. Fix it. #bug","2023-10-06 10:45:00",2,0,"#bug",-0.9
```

---

```
UserID,Username,AgeGroup,Country,Verified
1,@techie42,Adult,US,True
2,@critic99,Senior,UK,False
3,@daily_vibes,Teen,India,False
4,@designer_dan,Adult,Canada,True
5,@rage_user,Adult,US,False
```

---



## **Assignment Tasks**

You are required to complete the following three analysis tasks using Spark Structured APIs. Ensure that your analysis is well-documented, with clear explanations and any relevant visualizations or summaries.

### **1. Hashtag Trends **

**Objective:**

Identify trending hashtags by analyzing their frequency of use across all posts.

**Tasks:**

- **Extract Hashtags**: Split the `Hashtags` column and flatten it into individual hashtag entries.
- **Count Frequency**: Count how often each hashtag appears.
- **Find Top Hashtags**: Identify the top 10 most frequently used hashtags.


**Expected Outcome:**  
A ranked list of the most-used hashtags and their frequencies.

**Example Output:**

| Hashtag     | Count |
|-------------|-------|
| #tech       | 120   |
| #mood       | 98    |
| #design     | 85    |

---

### **2. Engagement by Age Group**

**Objective:**  
Understand how users from different age groups engage with content based on likes and retweets.

**Tasks:**

- **Join Datasets**: Combine `posts.csv` and `users.csv` using `UserID`.
- **Group by AgeGroup**: Calculate average likes and retweets for each age group.
- **Rank Groups**: Sort the results to highlight the most engaged age group.

**Expected Outcome:**  
A summary of user engagement behavior categorized by age group.

**Example Output:**

| Age Group | Avg Likes | Avg Retweets |
|-----------|-----------|--------------|
| Adult     | 67.3      | 25.2         |
| Teen      | 22.0      | 5.6          |
| Senior    | 9.2       | 1.3          |

---

### **3. Sentiment vs Engagement**

**Objective:**  
Evaluate how sentiment (positive, neutral, or negative) influences post engagement.

**Tasks:**

- **Categorize Posts**: Group posts into Positive (`>0.3`), Neutral (`-0.3 to 0.3`), and Negative (`< -0.3`) sentiment groups.
- **Analyze Engagement**: Calculate average likes and retweets per sentiment category.

**Expected Outcome:**  
Insights into whether happier or angrier posts get more attention.

**Example Output:**

| Sentiment | Avg Likes | Avg Retweets |
|-----------|-----------|--------------|
| Positive  | 85.6      | 32.3         |
| Neutral   | 27.1      | 10.4         |
| Negative  | 13.6      | 4.7          |

---

### **4. Top Verified Users by Reach**

**Objective:**  
Find the most influential verified users based on their post reach (likes + retweets).

**Tasks:**

- **Filter Verified Users**: Use `Verified = True` from `users.csv`.
- **Calculate Reach**: Sum likes and retweets for each user.
- **Rank Users**: Return top 5 verified users with highest total reach.

**Expected Outcome:**  
A leaderboard of verified users based on audience engagement.

**Example Output:**

| Username       | Total Reach |
|----------------|-------------|
| @techie42      | 1650        |
| @designer_dan  | 1320        |

---

**Task1 code explanation**
Explanation:

This PySpark script analyzes hashtag trends from a CSV file. It extracts individual hashtags, counts their occurrences, sorts them in descending order, and saves the results as a CSV file.

Key Steps:

Initialize Spark → SparkSession.builder.appName("HashtagTrends").getOrCreate()

Load Data → spark.read.option("header", True).csv("input/posts.csv")

Extract Hashtags → split(col("Hashtags"), ","), explode()

Count & Sort → groupBy("hashtag").count().orderBy(col("count").desc())

Save Output → coalesce(1).write.mode("overwrite").csv("outputs/hashtag_trends.csv", header=True)

Summary of Workflow:

Load the posts data from input/posts.csv.

Extract individual hashtags from the Hashtags column.

Count occurrences of each hashtag.

Sort the hashtags by frequency in descending order.

Save the results as a CSV file.

**output**

```
hashtag,count
"#tech",26
"#AI",22
"#social",22
"#UX",21
"#bug",21
"#cleanUI",20
"#design",20
"#mood",19
"#love",16
"#fail",12
```

**Task2 code explanation**

Explanation:

This PySpark script analyzes user engagement on social media by age group. It joins user and post datasets, calculates the average likes and retweets per age group, and saves the results as a CSV file.

Key Steps:

Initialize Spark → SparkSession.builder.appName("EngagementByAgeGroup").getOrCreate()

Load Data → spark.read.option("header", True).csv("input/posts.csv", inferSchema=True)

Join Datasets → posts_df.join(users_df, "UserID")

Group & Aggregate → groupBy("AgeGroup").agg(avg(col("Likes")), avg(col("Retweets")))

Sort Results → orderBy(col("AvgLikes").desc())

Save Output → coalesce(1).write.mode("overwrite").csv("outputs/engagement_by_age.csv", header=True)

Summary of Workflow:

Initialize Spark Session – Set up Spark for processing.

Load Data – Read posts.csv and users.csv with headers and inferred schema.

Join Datasets – Merge posts and users using the UserID column.

Group & Aggregate – Group data by AgeGroup, compute average likes and retweets.

Sort Results – Arrange age groups by highest average likes.

Save Output – Store results in outputs/engagement_by_age.csv.

**output**

```
AgeGroup,AvgLikes,AvgRetweets
Senior,76.25396825396825,25.095238095238095
Adult,71.57894736842105,32.10526315789474
Teen,70.38888888888889,31.444444444444443
```

**Task3 code explanation**

Explanation:

This PySpark script analyzes the relationship between post sentiment and engagement (likes & retweets). It categorizes posts into Positive, Neutral, and Negative based on sentiment scores, calculates average engagement metrics, and saves the results as a CSV file.

Key Steps:

Initialize Spark → SparkSession.builder.appName("SentimentVsEngagement").getOrCreate()

Load Data → spark.read.option("header", True).csv("input/posts.csv", inferSchema=True)

Categorize Sentiment

when(col("SentimentScore") > 0.3, "Positive")

when(col("SentimentScore") < -0.3, "Negative")

.otherwise("Neutral")

Group & Aggregate → groupBy("Sentiment").agg(avg("Likes"), avg("Retweets"))

Sort Results → orderBy("Sentiment")

Save Output → coalesce(1).write.mode("overwrite").csv("outputs/sentiment_engagement.csv", header=True)

Summary of Workflow:

Initialize Spark Session – Set up Spark for processing.

Load Posts Data – Read posts.csv with headers and inferred schema.

Classify Sentiment – Label posts as Positive, Neutral, or Negative based on SentimentScore.

Compute Engagement Metrics – Calculate average likes & retweets for each sentiment group.

Sort Results – Organize by sentiment category.

Save Output – Store results in outputs/sentiment_engagement.csv.

**output**
```
Sentiment,AvgLikes,AvgRetweets
Negative,78.9090909090909,27.727272727272727
Neutral,68.07692307692308,30.5
Positive,74.5609756097561,25.585365853658537

```

**Task4 code explanation**

Explanation:

This PySpark script identifies the top 5 verified users with the highest engagement (reach) on social media. It calculates reach as the sum of likes and retweets, aggregates the total reach per verified user, and saves the results.

Key Steps & Keywords:

Initialize Spark → SparkSession.builder.appName("TopVerifiedUsers").getOrCreate()

Load Data → spark.read.option("header", True).csv("input/posts.csv", inferSchema=True)

Filter Verified Users → users_df.filter(col("Verified") == True)

Join Datasets → posts_df.join(verified_users_df, "UserID")

Calculate Reach → withColumn("Reach", col("Likes") + col("Retweets"))

Aggregate Total Reach → groupBy("Username").agg(sum("Reach").alias("TotalReach"))

Sort & Select Top 5 → orderBy(col("TotalReach").desc()).limit(5)

Save Output → coalesce(1).write.mode("overwrite").csv("outputs/top_verified_users.csv", header=True)

Summary of Workflow:

Initialize Spark Session – Set up Spark for processing.

Load Datasets – Read posts.csv and users.csv with headers and inferred schema.

Filter Verified Users – Select only users with Verified == True.

Join Data – Merge posts_df with verified_users_df using UserID.

Compute Reach – Calculate reach (Likes + Retweets) for each post.

Aggregate Reach Per User – Sum up reach for each verified user.

Find Top 5 Users – Sort by TotalReach in descending order and select the top 5.

Save Output – Store results in outputs/top_verified_users.csv.

**output**

```
Username,TotalReach
@pixel_pusher,1314
@daily_vibes,980
@rage_user,969
@meme_lord,840
@designer_dan,736

```

## **Grading Criteria**

| Task                        | Marks |
|-----------------------------|-------|
| Hashtag Trend Analysis      | 1     |
| Engagement by Age Group     | 1     |
| Sentiment vs Engagement     | 1     |
| Top Verified Users by Reach | 1     |
| **Total**                   | **1** |

---

## 📬 Submission Checklist

- [ ] PySpark scripts in the `src/` directory  
- [ ] Output files in the `outputs/` directory  
- [ ] Datasets in the `input/` directory  
- [ ] Completed `README.md`  
- [ ] Commit everything to GitHub Classroom  
- [ ] Submit your GitHub repo link on canvas

---

Now go uncover the trends behind the tweets 📊🐤✨
