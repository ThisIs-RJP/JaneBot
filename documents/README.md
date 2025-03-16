# Introduction

## 1.1 Overview
JaneBot is a product that revolves around monitoring a user's screen time on their computers. The bot will detect the activities of users through the official Discord API, analyse the data, and perform different processes based off the data collected to be displayed through a web application.

JaneBot aims to inform its users the metrics in relation to their time on their computer, show how long they've spent on it and provide insights and recommendations from the data.

## 1.2 Purpose

The purpose of JaneBot is to provide a simple method for users to track their screen time and other metrics. It relieves the idea of having to download an entirely different application by simplifying it down to just one single Discord bot.

## 1.3 Scope

Scope of JaneBot

1. Track how long a user spends on their computer
> It is a safe assumption that the newer generation of young adults who spend time on their computers will always have Discord open in the background. This is more evident for programmers and gamers. We can use Discord as a medium to allow us to track how long a user might be spending on their computer by tracking the difference in time from when they first appear online until they appear offline.

2. Analyse the data and provide recommendations for users
> We want to be able to recommend users to new games based off the data collected from the bot. For example, if a user is spotted playing Valorant, JaneBot will utilise a machine learning model to recommend the user similar games, which in this case could be CSGO.

> Additionally, we should also provide challenges for users who aim to get better at certain games. For instance, after the signup, we will ask users to provide some games that they would like to play, see which games they would like otto improve in, then provide challenges for them that might help them improve. By setting goals like these, we hope to help our users also get better at the games they play.
    
2. Warn users that may be spending too much time on their computers
> During signup, we can prompt users to provide a certain time frame that they would like to be online for before being notified for exceeding their own screen limit. This may seem counterproductive based off the details from the last point, but our target audience is not only for people who are looking to improve in games, but also for people who just play games casually.

4. Provide a simple method to be able to inform users of the details they would like
> We aim to deploy a full stack application online for all people to be able to access (after logging in). This makes it easier for people to see their data whenever they want
    

## 1.4 Possible competitors

It is already very evident that we will be competing against a multitude of different desktop applications that track screen time. 

> The edge that JaneBot has is that it provides a universal method to be able to track screen time, without having to install the same application again. For example, if you have 2 devices (maybe a laptop and a desktop PC), you will have to download your screen time tracker application on both, as opposed to just having Discord. This in turn, will also end up consuming more memory on your computer for having another background process. With JaneBot, as long as you are using Discord, we will be able to provide that service to you.


A list of competitors include
- ActivityWatch
- Clockify
- It's FOSS