using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using IronPython.Hosting;
using Microsoft.Scripting.Hosting;

namespace CSharpWithPython
{
    // You can host the IronPython interpreter right in your .NET application
    // ref: https://stackoverflow.com/questions/13231913/how-do-i-call-a-specific-method-from-a-python-script-in-c
    // ref: https://medium.com/@dpursanov/running-python-script-from-c-and-working-with-the-results-843e68d230e5
    class Program
    {
        static void Main(string[] args)
        {
            // ExecuteIronPython();
            // ExecuteIronPython2();            
            ExecuteIronPython3();
        }
        
        private static void ExecuteIronPython()
        {

            // option 1
            var engine = Python.CreateEngine();
            dynamic scope = engine.CreateScope();

            scope.Add = new Func<int, int, int>((x, y) => x + y);
            Console.WriteLine(scope.Add(2, 3));

            // option 2

            var theScript = @"def PrintMessage():
                                print 'This is a message!'

PrintMessage()
                            ";

            engine.Execute(theScript);

            engine.Execute(@"print Add(2, 3)", scope);

            // option 3
            var filePath = @"C:\Jini\git\Python\CSharpWithPython\PythonApplication1\calledFromCSharp\function.py";
            // var filePath = @"G:\Jini\git\Python\PythonApplication_wikidocs_netbook1\function.py";
            engine.ExecuteFile(filePath, scope);

            // variables and functions defined in the scrip are added to the scope
            var result = scope.sum(2, 8);
            Console.WriteLine(result);

            // option 4
            dynamic builtin = engine.GetBuiltinModule();
            // you can store variables if you want
            dynamic list = builtin.list;

            dynamic itertools = engine.ImportModule("itertools");
            var numbers = new[] { 1, 2, 3, 4, 5, 6, 2, 2 };
            Console.WriteLine(builtin.str(list(itertools.chain(numbers, "foobar"))));


        }

        //ref: https://medium.com/@dpursanov/running-python-script-from-c-and-working-with-the-results-843e68d230e5
        //private static string PatchParameter(string parameter, int serviceid)
        //{
        //    var engine = Python.CreateEngine(); // Extract Python language engine from their grasp
        //    var scope = engine.CreateScope(); // Introduce Python namespace (scope)
        //    var d = new Dictionary<string, object>
        //    {
        //        { "serviceid", serviceid},
        //        { "parameter", parameter}
        //    }; // Add some sample parameters. Notice that there is no need in specifically setting the object type, interpreter will do that part for us in the script properly with high probability

        //    scope.SetVariable("params", d); // This will be the name of the dictionary in python script, initialized with previously created .NET Dictionary
        //    ScriptSource source = engine.CreateScriptSourceFromFile("PATH_TO_PYTHON_SCRIPT_FILE"); // Load the script
        //    object result = source.Execute(scope);
        //    parameter = scope.GetVariable<string>("parameter"); // To get the finally set variable 'parameter' from the python script
        //    return parameter;
        //}

        private static void ExecuteIronPython2()
        {
            var engine = Python.CreateEngine();
            dynamic scope = engine.CreateScope();
            // option 3
            var filePath = @"C:\Jini\git\Python\CSharpWithPython\PythonApplication1\calledFromCSharp\function.py";
            // var filePath = @"G:\Jini\git\Python\PythonApplication_wikidocs_netbook1\function.py";
            engine.ExecuteFile(filePath, scope);

            List<string> x = new List<string> { "aaa", "bbb", "ccc" };

            var result = scope.aaa(x);
            foreach (var member in result)
            {
                Console.WriteLine(member.ToString());
            }
        }

        private static void ExecuteIronPython3()
        {
            // ref: https://stackoverflow.com/questions/31369279/is-there-any-way-to-debug-python-code-embedded-in-c-sharp-with-visual-studio-and
            // NOTE: disabling "Just my code" in the Debug options allowed for debugging embedded Python, 
            // including breakpoints and stepping through it.
            var options = new Dictionary<string, object> { ["Debug"] = true };
            var engine = Python.CreateEngine(options);


            dynamic scope = engine.CreateScope();
            // option 3
            var filePath = @"C:\Jini\git\Python\CSharpWithPython\PythonApplication1\calledFromCSharp\parser.py";
            // var filePath = @"G:\Jini\git\Python\PythonApplication_wikidocs_netbook1\function.py";
            engine.ExecuteFile(filePath, scope);

            var parseDefintionData = new ParseDefinitionData {
                 ExclusiveReceiptPhrases = new List<string> { "" }
            };


            var receiptString = "xxxxx 23423gq345235yt23523gq5423gh234";
            receiptString = scope.preParse(parseDefintionData, receiptString);

            Console.WriteLine(receiptString);
        }
    }

    public class ParseDefinitionData
    {
        public List<string> ExclusiveReceiptPhrases { get; set; }
        public List<string> RemovedList { get; set; }
        public Dictionary<string, string> ReceiptReplaceList { get; set; }
        public List<string> ExclusivePhrases { get; set; }        public List<string> InclusivePhrases { get; set; }        public List<string> ItemColumnNames { get; set; }        public string ItemStartLineNo { get; set; }        public string ItemEndLineText { get; set; }
        public List<string> SummaryDataStart { get; set; }
        public List<string> SummaryDataEnd { get; set; }
        public List<string> SummaryDataExclusivePhrases { get; set; }
        public List<string> DetailDataExclusivePhrases { get; set; }        
    }
}
