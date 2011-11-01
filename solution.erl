%%%============================================================================
%%% WARNING / DISCLAIMER:
%%% This is my first Erlang "program" other then some Project Euler problems
%%% I've done last week. So take it for what it is - probably not the
%%% prettiest way to do this in Erlang, but it works, so at least THAT is a
%%% good thing :) Hopefully will be educationally useful for people to compare
%%% how things are done in different paradigms.
%%%
%%% FYI:
%%% Unfortunately there's no decimal type in Erlang STDLIB, so a 3rd party
%%% library would need to be used for real world math (top Google hit is this:
%%% https://github.com/tim/erlang-decimal). I just used float here for
%%% simplicity's sake.
%%%
%%% -- Siraaj Khandkar
%%%============================================================================


-module(solution).
-export([start/0]).


%%----------------------------------------------------------------------------
%% "Main" entry point
%%----------------------------------------------------------------------------
start() ->
    % Read data files
    PurchaseData = read_data("data/portfolio.dat"),
    PriceData = read_data("data/prices.dat"),

    % Extract portfolio and its cost
    {Portfolio, InitialCost} = portfolio_and_cost(PurchaseData),

    % Extract current price data
    CurrentPrices = dict:from_list(
        [{Stock, list_to_float(Price)} || {Stock, Price} <- PriceData]
    ),

    % Lookup current prices and calculate total current value
    FinalValue = lists:sum(
        [
            Shares * dict:fetch(Stock, CurrentPrices) ||
            {Stock, Shares} <- dict:to_list(Portfolio)
        ]
    ),

    % Print the reults!
    io:format("INITIAL COST:\t~p\n", [InitialCost]),
    io:format("FINAL VALUE:\t~p\n", [FinalValue]),
    io:format("-------------------------~n"),
    io:format("DIFFERENCE\t~p\n", [FinalValue - InitialCost]).


%%----------------------------------------------------------------------------
%% Helper functions
%%----------------------------------------------------------------------------
read_data(Path) ->
    {ok, FileBin} = file:read_file(Path),
    FileText = binary_to_list(FileBin),
    FileLines = string:tokens(FileText, "\n"),
    DataLists = [string:tokens(L, " ") || L <- FileLines],
    % Need to convert to tuples so that it can be converted to a dict laster
    DataTuples = [list_to_tuple(L) || L <- DataLists],
    DataTuples.


%% Extract unique stock names, initializing shares to 0
portfolio_and_cost(PurchaseData) ->
    Stocks = sets:to_list(sets:from_list(
        [{Stock, 0} || {Stock, _, _} <- PurchaseData]
    )),
    Portfolio = dict:from_list(Stocks),
    Spendings = [],
    portfolio_and_cost(PurchaseData, Portfolio, Spendings).


%% Now accumulate shares and purchasing cost
portfolio_and_cost([], Portfolio, Spendings) ->
    {Portfolio, lists:sum(Spendings)};

portfolio_and_cost(PurchaseData, Portfolio, Spendings) ->
    [Purchase|RemainingPurchases] = PurchaseData,
    {Stock, SharesString, PriceString} = Purchase,
    SharesPurchased = list_to_integer(SharesString),
    Price = list_to_float(PriceString),
    Cost = SharesPurchased * Price,
    UpdatedPortfolio = dict:update(
        Stock,
        fun(Shares) -> Shares + SharesPurchased end,
        Portfolio
    ),
    portfolio_and_cost(
        RemainingPurchases,
        UpdatedPortfolio,
        [Cost|Spendings]
    ).
