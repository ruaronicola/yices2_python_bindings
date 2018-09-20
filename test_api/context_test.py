import unittest

from ..yices_api import (
    yices_init,
    yices_exit,
    yices_new_config,
    yices_set_config,
    yices_new_context,
    yices_default_config_for_logic,
    yices_context_status,
    yices_push,
    yices_pop,
    yices_reset_context,
    yices_context_enable_option,
    yices_context_disable_option,
    yices_bool_type,
    yices_new_variable,
    yices_bv_type,
    yices_assert_formula,
    yices_set_term_name,
    yices_assert_formulas,
    YicesAPIException,
    yices_new_uninterpreted_term,
    yices_parse_term,
    make_term_array,
    yices_check_context,
    yices_assert_blocking_clause,
    yices_stop_search,
    yices_new_param_record,
    yices_default_params_for_context,
    yices_set_param,
    yices_free_param_record,
    yices_free_context,
    yices_free_config,
    STATUS_SAT
    )


class TestContext(unittest.TestCase):

    def setUp(self):
        yices_init()

    def tearDown(self):
        yices_exit()

    def test_config(self):
        cfg = yices_new_config()
        # Valid call
        yices_set_config(cfg, "mode", "push-pop")
        # Invalid name
        with self.assertRaisesRegexp(YicesAPIException, 'invalid parameter'):
            yices_set_config(cfg, "baz", "bar")
        # Invalid value
        with self.assertRaisesRegexp(YicesAPIException, 'value not valid for parameter'):
            yices_set_config(cfg, "mode", "bar")
        yices_default_config_for_logic(cfg, "QF_UFNIRA")
        yices_free_config(cfg)

    def test_context(self):
        cfg = yices_new_config()
        ctx = yices_new_context(cfg)
        stat = yices_context_status(ctx)
        ret = yices_push(ctx)
        ret = yices_pop(ctx)
        yices_reset_context(ctx)
        ret = yices_context_enable_option(ctx, "arith-elim")
        ret = yices_context_disable_option(ctx, "arith-elim")
        stat = yices_context_status(ctx)
        self.assertEqual(stat, 0)
        yices_reset_context(ctx)
        bool_t = yices_bool_type()
        bvar1 = yices_new_variable(bool_t)
        with self.assertRaisesRegexp(YicesAPIException, 'assertion contains a free variable'):
            yices_assert_formula(ctx, bvar1)
        bv_t = yices_bv_type(3)
        bvvar1 = yices_new_uninterpreted_term(bv_t)
        yices_set_term_name(bvvar1, 'x')
        bvvar2 = yices_new_uninterpreted_term(bv_t)
        yices_set_term_name(bvvar2, 'y')
        bvvar3 = yices_new_uninterpreted_term(bv_t)
        yices_set_term_name(bvvar3, 'z')
        fmla1 = yices_parse_term('(= x (bv-add y z))')
        fmla2 = yices_parse_term('(bv-gt y 0b000)')
        fmla3 = yices_parse_term('(bv-gt z 0b000)')
        yices_assert_formula(ctx, fmla1)
        yices_assert_formulas(ctx, 3, make_term_array([fmla1, fmla2, fmla3]))
        smt_stat = yices_check_context(ctx, None)
        self.assertEqual(smt_stat, STATUS_SAT)
        yices_assert_blocking_clause(ctx)
        yices_stop_search(ctx)
        param = yices_new_param_record()
        yices_default_params_for_context(ctx, param)
        yices_set_param(param, "dyn-ack", "true")
        with self.assertRaisesRegexp(YicesAPIException, 'invalid parameter'):
            yices_set_param(param, "foo", "bar")
        with self.assertRaisesRegexp(YicesAPIException, 'value not valid for parameter'):
            yices_set_param(param, "dyn-ack", "bar")
        yices_free_param_record(param)
        yices_free_context(ctx)


if __name__ == '__main__':
    unittest.main()