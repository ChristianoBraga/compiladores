local function make_printer()
  local a = 100
  return function()
    print("Lexical scoping:", a)
    print("Dynamic scoping:", dynamic(a))
  end
end

local function run_func(fn)
  local a = 200
  fn()
end

local print_a = make_printer()

run_func(print_a)
-- prints:
-- Lexical scoping: 100
-- Dynamic scoping: 20