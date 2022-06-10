# Dungeon Crawl (sprint 2)

## Story

Last week you created a pretty good [Roguelike](https://en.wikipedia.org/wiki/Roguelike) game.
It already has some features, but the players have no opportunity to save their games.
It can be annoying, especially when you have to leave the game suddenly.

The gamer community is begging you for saving functionality and some other new and interesting ideas, such as:

- game sharing between players
- maps of different sizes
- player-tracking camera movement

Management is handing out a **prioritized list** of new user stories that must be
appended to the unfinished stories from last week in your product backlog.
Try to estimate these new stories as well, and, based on the estimations,
pick the stories your team can finish in this sprint.

> Using database for saving game state feature is a business critical item which overrides every other priority now!

Continue this entertaining project and make our players happier!

## What are you going to learn?

- Serialize objects.
- Communicate with databases.
- Write unit tests for your classes.
- Understand the **Data Access Object** design pattern.

## Tasks

1. Create a new sprint from the existing backlog. Last week, you had a long list of stories, and there are a few new stories this week.
    - The new items are added to the backlog.
    - The team has created a new sprint plan, based on the unified backlog.
    - The mandatory "Saving game" backlog item is in Sprint 2 and planned in detail.

2. As you work in a new repository, but need the code from the previous sprint, add the `dungeon-crawl-2` repository as a new remote to the repository of the previous sprint, then pull (merge) and push your changes into it.
    - There is a merge commit in the project repository that contains code from the previous sprint.

3. Allow the user to save the current state of the game in a database. Extend the given schema if needed.
    - The application uses SQL Server database with the schema in `schema_ddl.sql`.
    - The application respects the `MSSQL_USER_NAME`, `MSSQL_PASSWORD`, and `MSSQL_DB_NAME` environment variables.
    - An Entity Relationship diagram (connections between classes, 1-1, 1-many, and so on) is created in a digitalized format.
    - When the user presses `F5`, the game saves the current state (current map, player position, and inventory content) in the database, overwriting the old game state (if there is one in the database). In the corner of the screen, a UI text displays "Game saved." for 5 seconds.
    - Already discovered maps are also saved in the DB.
    - When the user presses `F9`, the game loads the previously saved state (map, position, and inventory). After loading, in the corner of the screen, a UI text displays "Game loaded." for 5 seconds. 

4. Allow the user to export (serialize) their game state into a text file, and load (deserialize) the game from the exported file.
    - Pressing `F10` triggers the export mechanism.
    - The export process creates the exported file in the `exported_saves` subfolder in the main directory of the game. The file name is generated with the following pattern: `<game-name>_<save's-date-and-hour>.json`.
    - The file stores every necessary game state information in a JSON format.
    - Pressing `F11` imports the last exported game (it selects the file based on the date and hour in the file name). If the chosen file is not in the proper format, the game displays an "IMPORT ERROR!" message on UI, in the corner of the screen.

5. The customer looks for quality assurance and wants to see that your code is covered by unit tests. It is important to also cover negative scenarios, not only positive test cases.
    - Every unit test method is well-arranged and follows the `arrange`-`act`-`assert` structure.
    - Unit test classes and methods adhere to the following naming conventions consistently.
- classes: `<The name of the tested class>Test`
- methods: `<the name of the tested method>_<expected input / tested state>_<expected behavior>`
    - Every test class has at least one negative test case (or more, if it is plausible).
    - Code coverage of self-created business logic classes is above 90%.

## General requirements

None

## Hints

- Break down the backlog items into smaller tasks so that you can work in parallel.
- The given DB schema is only an example. You probably need to alter it,
  according to the requirements. For example, it doesn't contain any information
  on the inventory, or on maps discovered by the player.
- Write as many unit tests as possible to cover your business logic.
- Set up a test for getting `null` as an argument for methods that take a reference type parameter. These are called negative test cases.
- Unity C# projects don't support NuGets and direct project references. In order to be able to use the SQL Server
  classes, take the `System.Data.dll` file from the start repo and put it in the `Assets` subfolder of your Unity project. Upon refreshing the C# solution, you should be able to work with SQL Server databases just fine.
- Read the value of an environment variable' using `System.GetEnvironmentVariable("VAR_NAME");`.
- View and edit environment variables in [Visual Studio](https://www.tutorialsteacher.com/core/aspnet-core-environment-variable) and in [Rider](https://blog.jetbrains.com/dotnet/2017/08/23/rundebug-configurations-rider/).


## Background materials

- <i class="far fa-exclamation"></i> [Software testing](project/curriculum/materials/pages/general/software-testing.md)
- <i class="far fa-book-open"></i> [Positive or negative](https://stackoverflow.com/questions/8162423)
- <i class="far fa-exclamation"></i> [How to design classes](project/curriculum/materials/pages/csharp/how-to-design-classes.md)
- <i class="far fa-book-open"></i> [Unity Documentaton](https://docs.unity3d.com/Manual/index.html)
- <i class="far fa-exclamation"></i> [SQL in Visual Studio and CRUD operations](https://alexcodetuts.com/2019/04/26/how-to-connect-sql-server-database-using-c-and-perform-crud-operation-part-1/)
- <i class="far fa-exclamation"></i> [Obtaining data through SQL DataReader](https://docs.microsoft.com/en-us/dotnet/framework/data/adonet/retrieving-data-using-a-datareader)
- <i class="far fa-exclamation"></i> [JSON.NET](https://www.newtonsoft.com/json)
- [1-Bit Pack by Kenney](https://kenney.nl/assets/bit-pack)
