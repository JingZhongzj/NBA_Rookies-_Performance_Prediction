Project Title: NBA Rookies' Performance Prediction


Team Members:   Jing Zhong        jz2748
              	Zebin Wang      zw2364
                Junbo Chen       jc4648


Motivation: 
      The selection of rookies in NBA has great impacts on the whole team, so it is important for team managers to evaluate 
  rookies' future performance so that they can make correct choices. So we decide to make prediction about rookiesÕ 
  performance in the  future NBA career. That is how to do: Based on the relation between NBA players' performance in NCAA and 
  NBA, use rookies' performance in NCAA to predict their performance in future NBA career. 


Dataset:
      We used Python to grab data from http://www.basketball-reference.com/.
  Data for each NBA player - both active player and retired player, and NCAA player - both active player and retired 
  player. Games played, Minutes played, Field Goals, Points scored, Personal fouls, rebounds, turnovers, Points, etc.
  

Algorithm:
      We used the Multilayer Perceptron Classifier in the Machine Learning Library of Spark, we wrote the code using Python. 
  After we got the data, we calculated the "Simple PER" of each player, and narrowed them 4 different values, which are the 
  classes in the classification process.

Input: 
     Training data: 21 attributes (including points, rebounds, assists, steals, blocks, turnovers, field goals, etc) of every 
                 single NBA players when they were in NCAA. We also set "Simple PER" as the label of each player.
     Test data: 20% of the training data.
     Data for Prediction: 21 attributes of each current NCAA players.

Output:
    Future "Simple PER" of current NCAA players when they get in NBA.
