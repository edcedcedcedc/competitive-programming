string input = Console.ReadLine() ?? string.Empty;
string uniqualizedString = new string(input.Distinct().ToArray());
if(uniqualizedString.Length % 2 != 0)
{
    Console.WriteLine("IGNORE HIM!");
}
else
{
    Console.WriteLine("CHAT WITH HER!");
}