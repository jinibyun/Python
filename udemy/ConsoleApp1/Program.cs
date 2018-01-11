using IronPython.Hosting;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    // You can host the IronPython interpreter right in your .NET application
    // ref: https://stackoverflow.com/questions/13231913/how-do-i-call-a-specific-method-from-a-python-script-in-c
    // ref: https://medium.com/@dpursanov/running-python-script-from-c-and-working-with-the-results-843e68d230e5
    class Program
    {
        static void Main(string[] args)
        {     
            ExecuteIronPython();
        }

        private static void ExecuteIronPython()
        {
            // ref: https://stackoverflow.com/questions/31369279/is-there-any-way-to-debug-python-code-embedded-in-c-sharp-with-visual-studio-and
            // NOTE: disabling "Just my code" in the Debug options allowed for debugging embedded Python, 
            // including breakpoints and stepping through it.
            var options = new Dictionary<string, object> { ["Debug"] = true };
            var engine = Python.CreateEngine(options);

            dynamic scope = engine.CreateScope();
            // option 3           
            var filePath = @"C:\Jini\git\Python\CSharpWithPython\PythonApplication1\calledFromCSharp\a020atest333.py";

            // ref: https://stackoverflow.com/questions/14433393/compiling-all-files-c-ironpython
            //var paths = engine.GetSearchPaths();
            //paths.Add(@"C:\Jini\git\Python\CSharpWithPython\PythonApplication1\calledFromCSharp\");            
            //engine.SetSearchPaths(paths);

            // ref: https://stackoverflow.com/questions/1371994/importing-external-module-in-ironpython
            // NOTE: better than above
            string dir = Path.GetDirectoryName(filePath);
            ICollection<string> paths = engine.GetSearchPaths();

            if (!String.IsNullOrWhiteSpace(dir))
            {
                paths.Add(dir);
            }
            else
            {
                paths.Add(Environment.CurrentDirectory);
            }

            paths.Add(@"C:\Program Files (x86)\IronPython 2.7\Lib");
            engine.SetSearchPaths(paths);

            // engine.ExecuteFile(filePath, scope);
            var source = engine.CreateScriptSourceFromFile(filePath);
            source.Execute(scope);

            var parseDefintionData = new ParseDefinitionData
            {
                // ExclusiveReceiptPhrases = new List<string> { "Datametrex", "yyyyy" },
                ItemStartLineNo = "6",
                ItemEndLineText = "Thank you for shopping",
                SummaryDataStart = new List<string> { "SUBTOTAL" },
                SummaryDataEnd = new List<string> { "CHANGE", "PAID", "TOTAL" },
                SummaryDataExclusivePhrases = new List<string> { "-------", "PAID", "TOTAL" },

                DetailParameter = new ParameterDetail
                {
                    UnitPriceSuffix = new List<string> { "TB" },
                    IgnoreStartPoistion = -1,
                    itemCodepattern = "^[0-9]+",
                    isExistItemCode = true,
                    customDelimeter = "~~"
                },
                SummaryParameter = new ParameterSummary
                {
                    ReplaceList = new Dictionary<string, string>
                     {
                         { "TOTAL SALE", "TOTAL" },
                         { "DEBIT CARD", "DEBITCARD" },
                         { "BALANCE DUE", "CHANGE" }
                     }
                },
                DetailLines = new DetailLine()
                {
                    Lines = new List<Line>
                     {
                          new Line
                          {
                              Items = new List<Item>
                              {
                                  new Item { Attribute = new attribute{ empty = "NOT NULL", order ="0", type="nvarchar(50)" }, Value = "InventoryId" },
                                  new Item { Attribute = new attribute{ empty = "NOT NULL", order ="1", type="nvarchar(200)" }, Value = "ProductName" },
                                  new Item { Attribute = new attribute{ empty = "NOT NULL", order ="2", type="decimal(18,2)" }, Value = "Qty" },
                                  new Item { Attribute = new attribute{ empty = "NOT NULL", order ="3", type="decimal(18,2)" }, Value = "UnitPrice" },
                                  new Item { Attribute = new attribute{ empty = "NULL", order ="4", type="nvarchar(20)" }, Value = "TaxSignature" },
                                  new Item { Attribute = new attribute{ empty = "NOT NULL", order ="5", type="decimal(18,2)" }, Value = "Price" }
                              }
                          }
                     }
                },
                SummaryLines = new SummaryLine
                {
                    Lines = new List<Line>
                     {
                          new Line
                          {
                              Items = new List<Item>
                              {
                                   new Item { Attribute = new attribute{ empty = "NULL", order ="0", type="decimal(18,2)" }, Value = "SUBTOTAL" }
                              }
                          },
                          new Line
                          {
                              Items = new List<Item>
                              {
                                   new Item { Attribute = new attribute{ empty = "NULL", order ="1", type="decimal(18,2)" }, Value = "GST" }
                              }
                          },
                          new Line
                          {
                              Items = new List<Item>
                              {
                                   new Item { Attribute = new attribute{ empty = "NULL", order ="2", type="decimal(18,2)" }, Value = "PST" }
                              }
                          },
                          new Line
                          {
                              Items = new List<Item>
                              {
                                   new Item { Attribute = new attribute{ empty = "NULL", order ="3", type="decimal(18,2)" }, Value = "TOTAL" }
                              }
                          },
                          new Line
                          {
                              Items = new List<Item>
                              {
                                   new Item { Attribute = new attribute{ empty = "NULL", order ="4", type="decimal(18,2)" }, Value = "CHANGE" }
                              }
                          },
                          new Line
                          {
                              Items = new List<Item>
                              {
                                   new Item { Attribute = new attribute{ empty = "nvarchar(20)", order ="5", type="decimal(18,2)" }, Value = "PAID" }
                              }
                          },
                          new Line
                          {
                              Items = new List<Item>
                              {
                                   new Item { Attribute = new attribute{ empty = "nvarchar(20)", order ="6", type="decimal(18,2)" }, Value = "PayMethod" }
                              }
                          },
                          new Line
                          {
                              Items = new List<Item>
                              {
                                   new Item { Attribute = new attribute{ empty = "decimal(18,2)", order ="7", type="decimal(18,2)" }, Value = "PayAmount" }
                              }
                          }
                     }
                }
            };

            var receiptString = @"
            Datametrex Demo             

        OCTOBER 16, 2017   11:56        
      SALE #POS-3165     S/P-STAFF      
----------------------------------------
034000003402 CAMEL                      
              1.00 @ 12.99         12.99
034000003402 COCA COLA CLASSIC          
              1.00 @ 0.99           0.99

                   SUBTOTAL        13.98
 SALE        13.98
                  PAID CASH        13.98
----------------------------------------
         Thank you for shopping         
.
.
.
d0
";
            var rp = scope.receiptParser();
            rp.parseDefinitionData = parseDefintionData;
            rp.receiptString = receiptString;

            rp.Parse();
            
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
        public ParameterDetail DetailParameter { get; set; }
        public ParameterSummary SummaryParameter { get; set; }

        public DetailLine DetailLines { get; set; }
        public SummaryLine SummaryLines { get; set; }
    }

    public class ParameterDetail
    {
        public List<string> SalePriceSuffix { get; set; }
        public List<string> UnitPriceSuffix { get; set; }
        public List<string> RemovedList { get; set; }
        public int IgnoreStartPoistion { get; set; }
        public Dictionary<string, string> ReplaceList { get; set; }
        public string itemCodepattern { get; set; }
        public bool isExistItemCode { get; set; }
        public string customDelimeter { get; set; }
    }

    public class ParameterSummary
    {
        public Dictionary<string, string> ReplaceList { get; set; }
    }

    public class DetailLine
    {
        public List<Line> Lines { get; set; }
    }

    public class SummaryLine
    {
        public List<Line> Lines { get; set; }
    }

    public class Line
    {
        public List<Item> Items { get; set; }
    }

    public class Item
    {
        public string Value { get; set; }
        public attribute Attribute { get; set; }
    }

    public class attribute
    {
        public string type { get; set; }
        public string empty { get; set; }
        public string order { get; set; }
    }

    public class MassageParameter
    {
        public string[] unnecessarySymbols = new string[] { "$" };
        public List<string> SalePriceSuffix { get; set; }
        public List<string> UnitPriceSuffix { get; set; }
        public List<string> RemovedList { get; set; }
        public int IgnoreStartPoistion { get; set; }
        public Dictionary<string, string> ReplaceList { get; set; }
        public string itemCodepattern { get; set; }
        public bool isExistItemCode { get; set; }
        public string customDelimeter { get; set; }
        public string description { get; set; }

        // summary
        public Dictionary<string, string> SummaryReplaceList { get; set; }
    }

}
